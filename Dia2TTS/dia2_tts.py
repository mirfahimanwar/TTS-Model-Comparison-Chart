"""
dia2_tts.py -- CLI for Dia2 TTS (github.com/nari-labs/dia2)

QUICK START:
  python dia2_tts.py "[S1] Hello world, this is Dia2 TTS."
  python dia2_tts.py "[S1] Hey! [S2] Hey yourself! [S1] (laughs) How are you?" --play
  python dia2_tts.py --interactive
  python dia2_tts.py "[S1] Hello." --prefix-s1 voice.wav

FULL USAGE:
  python dia2_tts.py <text>        [--out FILE] [--play] [--temp T]
                                   [--cfg-scale F] [--top-k N] [--seed N] [--cpu]
  python dia2_tts.py --interactive [--temp T] [--cfg-scale F]
  python dia2_tts.py <text>        --prefix-s1 AUDIO [--prefix-s2 AUDIO]

DIALOGUE FORMAT (required):
  Always start with [S1]. Alternate speakers with [S2].
  Example: "[S1] Hello! [S2] Hey, how are you? [S1] Doing great, thanks!"
  If you omit [S1], it is added automatically.

NON-VERBAL TOKENS:
  (laughs)  (chuckle)  (sighs)  (gasps)  (coughs)  (sneezes)  (sniffs)
  (clears throat)  (inhales)  (exhales)  (mumbles)  (humming)  (whistles)
  (singing)  (sings)  (groans)  (screams)  (claps)  (applause)  (burps)  (beep)
  Use sparingly -- overuse causes audio artifacts.

VOICE CLONING:
  --prefix-s1   path to reference WAV for speaker 1
  --prefix-s2   path to reference WAV for speaker 2 (optional, for 2-speaker dialogue)
  Whisper automatically transcribes the reference audio -- no --prompt-text needed!

GENERATION PARAMETERS:
  --temp        audio sampling temperature (default 0.8, min ~0.5)
  --cfg-scale   classifier-free guidance scale (default 2.0, keep <= 3.0)
  --top-k       top-k sampling (default 50)
  --cuda-graph  enable CUDA graph for faster generation (no MSVC required)

MODEL SIZES:
  nari-labs/Dia2-2B  (default, ~4 GB, better quality)
  nari-labs/Dia2-1B  (faster, ~2 GB)
  Pass with: --model nari-labs/Dia2-1B
"""

import argparse
import os
import sys
import time

import numpy as np
import soundfile as sf

# ── Optional playback ────────────────────────────────────────────────────────
try:
    import sounddevice as sd
    _HAS_SOUNDDEVICE = True
except ImportError:
    _HAS_SOUNDDEVICE = False

# ── dia2 lives in the dia2/ subdirectory (cloned repo, editable install) ─────
_HERE = os.path.dirname(os.path.abspath(__file__))
_DIA2_DIR = os.path.join(_HERE, "dia2")
if _DIA2_DIR not in sys.path:
    sys.path.insert(0, _DIA2_DIR)

REPO_ID = "nari-labs/Dia2-2B"

_model = None
_model_id = None


def _load_model(cpu: bool = False, model_id: str = REPO_ID) -> object:
    global _model, _model_id
    if _model is not None and _model_id == model_id:
        return _model
    import torch
    from dia2 import Dia2
    device = "cpu" if cpu else ("cuda" if torch.cuda.is_available() else "cpu")
    dtype = "float32" if device == "cpu" else "bfloat16"
    size_hint = "~4 GB" if "2B" in model_id else "~2 GB"
    print(f"Loading Dia2 model on {device} ({dtype}) ...")
    print(f"  First run downloads {size_hint} to ~/.cache/huggingface/")
    _model = Dia2.from_repo(model_id, device=device, dtype=dtype)
    _model_id = model_id
    return _model


def _ensure_speaker_tag(text: str) -> str:
    """Prefix [S1] if the text doesn't already start with a speaker tag."""
    stripped = text.strip()
    if not stripped.startswith("[S1]") and not stripped.startswith("[S2]"):
        return "[S1] " + stripped
    return stripped


def _generate(
    text: str,
    prefix_s1: str | None,
    prefix_s2: str | None,
    temp: float,
    cfg_scale: float,
    top_k: int,
    seed: int | None,
    cpu: bool,
    use_cuda_graph: bool,
    model_id: str,
) -> tuple[np.ndarray, int]:
    import torch
    if seed is not None:
        import random
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

    model = _load_model(cpu=cpu, model_id=model_id)

    from dia2 import GenerationConfig, SamplingConfig

    full_text = _ensure_speaker_tag(text)

    audio_sampling = SamplingConfig(temperature=temp, top_k=top_k)
    # Text tokens use a slightly lower temperature for more stable transcription
    text_sampling = SamplingConfig(temperature=min(temp, 0.6), top_k=top_k)

    config = GenerationConfig(
        audio=audio_sampling,
        text=text_sampling,
        cfg_scale=cfg_scale,
        use_cuda_graph=use_cuda_graph,
    )

    result = model.generate(
        full_text,
        config=config,
        prefix_speaker_1=prefix_s1,
        prefix_speaker_2=prefix_s2,
        verbose=True,
    )

    if result is None or result.waveform is None:
        raise RuntimeError("Model returned no audio.")

    waveform = result.waveform.detach().cpu()
    if waveform.ndim > 1:
        waveform = waveform.squeeze()
    audio_np = waveform.numpy()

    if len(audio_np) == 0:
        raise RuntimeError(
            "Model returned empty audio. cfg_scale may be too high (try <= 3.0) "
            "or temperature too low (try >= 0.5)."
        )

    return audio_np, result.sample_rate


def _save(audio: np.ndarray, sample_rate: int, out_path: str | None) -> str:
    if out_path is None:
        session = int(time.time())
        out_dir = os.path.join(_HERE, "output", f"session_{session}")
        os.makedirs(out_dir, exist_ok=True)
        existing = [f for f in os.listdir(out_dir) if f.endswith(".wav")]
        idx = len(existing) + 1
        out_path = os.path.join(out_dir, f"{idx:03d}.wav")
    else:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    sf.write(out_path, audio, sample_rate)
    duration = len(audio) / sample_rate
    print(f"  Saved -> {out_path}  ({duration:.2f}s)")
    return out_path


def _play(audio: np.ndarray, sample_rate: int) -> None:
    if not _HAS_SOUNDDEVICE:
        print("  (install sounddevice for --play support:  pip install sounddevice)")
        return
    sd.play(audio, sample_rate)
    sd.wait()


def _run_once(args) -> None:
    t0 = time.time()
    audio, sr = _generate(
        text=args.text,
        prefix_s1=getattr(args, "prefix_s1", None),
        prefix_s2=getattr(args, "prefix_s2", None),
        temp=args.temp,
        cfg_scale=args.cfg_scale,
        top_k=args.top_k,
        seed=args.seed,
        cpu=args.cpu,
        use_cuda_graph=args.cuda_graph,
        model_id=args.model,
    )
    _save(audio, sr, args.out)
    print(f"  Generated in {time.time() - t0:.1f}s")
    if args.play:
        _play(audio, sr)


def _run_interactive(args) -> None:
    print("Dia2 TTS -- interactive mode")
    print("  Speaker tags: [S1] speaker one   [S2] speaker two")
    print("  Non-verbals:  (laughs) (sighs) (gasps) (coughs) (clears throat)")
    print("  Commands:  /temp <value>       /cfg <value>        /top-k <n>")
    print("             /seed <n>           /noseed             /play  /noplay")
    print("             /prefix-s1 <path>   /prefix-s2 <path>   /noprefx")
    print("             /cuda-graph         /no-cuda-graph      /quit")
    print()

    temp = args.temp
    cfg_scale = args.cfg_scale
    top_k = args.top_k
    seed = args.seed
    play = args.play
    prefix_s1 = getattr(args, "prefix_s1", None)
    prefix_s2 = getattr(args, "prefix_s2", None)
    cuda_graph = args.cuda_graph

    # Pre-load model so first generation doesn't include load time
    _load_model(cpu=args.cpu, model_id=args.model)

    while True:
        try:
            line = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        if line.startswith("/"):
            parts = line.split(None, 1)
            cmd = parts[0].lower()
            val = parts[1].strip() if len(parts) > 1 else ""

            if cmd == "/quit":
                break
            elif cmd == "/temp":
                try:
                    temp = float(val)
                    print(f"  temp -> {temp}")
                except ValueError:
                    print("  Usage: /temp <float>")
            elif cmd == "/cfg":
                try:
                    cfg_scale = float(val)
                    print(f"  cfg_scale -> {cfg_scale}")
                except ValueError:
                    print("  Usage: /cfg <float>")
            elif cmd == "/top-k":
                try:
                    top_k = int(val)
                    print(f"  top_k -> {top_k}")
                except ValueError:
                    print("  Usage: /top-k <int>")
            elif cmd == "/seed":
                try:
                    seed = int(val)
                    print(f"  seed -> {seed}")
                except ValueError:
                    print("  Usage: /seed <int>")
            elif cmd == "/noseed":
                seed = None
                print("  seed cleared")
            elif cmd == "/play":
                play = True
                print("  playback enabled")
            elif cmd == "/noplay":
                play = False
                print("  playback disabled")
            elif cmd == "/prefix-s1":
                if val:
                    prefix_s1 = val
                    print(f"  prefix_s1 -> {val}")
                else:
                    print("  Usage: /prefix-s1 <path>")
            elif cmd == "/prefix-s2":
                if val:
                    prefix_s2 = val
                    print(f"  prefix_s2 -> {val}")
                else:
                    print("  Usage: /prefix-s2 <path>")
            elif cmd == "/noprefx":
                prefix_s1 = None
                prefix_s2 = None
                print("  voice prefix cleared")
            elif cmd == "/cuda-graph":
                cuda_graph = True
                print("  CUDA graph enabled")
            elif cmd == "/no-cuda-graph":
                cuda_graph = False
                print("  CUDA graph disabled")
            else:
                print(f"  Unknown command: {cmd}")
            continue

        t0 = time.time()
        try:
            audio, sr = _generate(
                text=line,
                prefix_s1=prefix_s1,
                prefix_s2=prefix_s2,
                temp=temp,
                cfg_scale=cfg_scale,
                top_k=top_k,
                seed=seed,
                cpu=args.cpu,
                use_cuda_graph=cuda_graph,
                model_id=args.model,
            )
            _save(audio, sr, args.out)
            print(f"  Generated in {time.time() - t0:.1f}s")
            if play:
                _play(audio, sr)
        except Exception as e:
            print(f"  Error: {e}")

    print("Bye!")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Dia2 TTS CLI -- streaming dialogue-aware text-to-speech",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("text", nargs="?", help="Text to synthesize (use [S1]/[S2] speaker tags)")
    parser.add_argument("--interactive", "-i", action="store_true", help="Interactive prompt loop")
    parser.add_argument("--out", "-o", metavar="FILE", help="Output WAV path (default: output/session_<t>/NNN.wav)")
    parser.add_argument("--play", action="store_true", help="Play audio immediately after generation")
    parser.add_argument("--prefix-s1", metavar="WAV", dest="prefix_s1", help="Reference WAV for speaker 1 voice cloning (auto-transcribed by Whisper)")
    parser.add_argument("--prefix-s2", metavar="WAV", dest="prefix_s2", help="Reference WAV for speaker 2 voice cloning (optional)")
    parser.add_argument("--temp", type=float, default=0.8, metavar="T", help="Audio sampling temperature (default: 0.8)")
    parser.add_argument("--cfg-scale", type=float, default=2.0, metavar="F", help="CFG guidance scale (default: 2.0, keep <= 3.0)")
    parser.add_argument("--top-k", type=int, default=50, metavar="N", dest="top_k", help="Top-k sampling (default: 50)")
    parser.add_argument("--seed", type=int, default=None, metavar="N", help="Random seed for reproducibility")
    parser.add_argument("--cuda-graph", action="store_true", dest="cuda_graph", help="Enable CUDA graph for faster generation (no MSVC required)")
    parser.add_argument("--model", default=REPO_ID, metavar="ID", help=f"HuggingFace model repo ID (default: {REPO_ID})")
    parser.add_argument("--cpu", action="store_true", help="Force CPU inference (very slow)")

    args = parser.parse_args()

    if not args.interactive and not args.text:
        parser.print_help()
        sys.exit(0)

    if args.interactive:
        _run_interactive(args)
    else:
        _run_once(args)


if __name__ == "__main__":
    main()

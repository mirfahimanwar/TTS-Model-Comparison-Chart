# Dia2TTS CLI

A clean one-click CLI wrapper for [Dia2 TTS](https://github.com/nari-labs/dia2) by Nari Labs.

Dia2 is a streaming dialogue TTS model (1B / 2B parameter). It generates highly realistic
multi-speaker audio from `[S1]` / `[S2]` tagged transcripts and supports voice cloning via an
audio prefix. **No transcript needed** — Whisper automatically transcribes your reference audio.

---

## What's new in Dia2 vs Dia1

| Feature | Dia1 | Dia2 |
|---|---|---|
| Voice cloning transcript | Manual (`--prompt-text`) | Auto (Whisper) |
| Max generation length | ~35s | ~2 minutes |
| Two-speaker voice prefix | No | Yes (`--prefix-s2`) |
| Codec | DAC | Kyutai Mimi |
| CUDA graph support | No (needs MSVC) | Yes (`--cuda-graph`) |
| Model sizes | 1.6B only | 1B / 2B |
| CUDA requirement | 12.4+ | 12.8+ |

---

## Quick Examples

```powershell
# Basic
python dia2_tts.py "[S1] Hello world, this is Dia2 TTS." --play

# Two speakers
python dia2_tts.py "[S1] Hey! [S2] Hey yourself! [S1] (laughs) How are you?" --play

# Voice clone — single line (no transcript needed, Whisper handles it)
# Use spaces between flag and value, not = signs
python dia2_tts.py "[S1] Hello, how are you?" --prefix-s1 "D:\path\to\voice.wav" --play

# Voice clone — interactive, pre-loaded at startup
python dia2_tts.py --interactive --play --prefix-s1 "D:\path\to\voice.wav"

# Interactive — set voice inside the session
python dia2_tts.py --interactive --play
# >>> /prefix-s1 D:\path\to\voice.wav
# >>> [S1] Now type whatever you want to generate.

# Faster generation (CUDA graph + 1B model)
python dia2_tts.py --interactive --play --cuda-graph --model nari-labs/Dia2-1B
```

> **Flag syntax:** always use a space between the flag and value — `--prefix-s1 "file.wav"` not `--prefix-s1="file.wav"`
> **Script name:** `dia2_tts.py` — always call it with `python dia2_tts.py`
> **No `--prompt-text`:** unlike Dia1, Whisper auto-transcribes your reference audio

---

## Requirements

- Python 3.10+
- Git
- NVIDIA GPU with CUDA 12.8+ drivers (`nvidia-smi` should show CUDA Version: 12.8)
- ~4 GB disk space for Dia2-2B (downloaded automatically on first run)

---

## Setup (Windows)

```powershell
git clone <this-repo> Dia2TTS
cd Dia2TTS
.\setup.ps1
.\venv\Scripts\Activate.ps1
```

`setup.ps1` will:
1. Clone [nari-labs/dia2](https://github.com/nari-labs/dia2) into `dia2/`
2. Create a Python virtual environment
3. Install PyTorch with CUDA 12.8
4. Install Dia2 and all dependencies (including Whisper for auto-transcription)
5. Install `sounddevice` for `--play` support

---

## Usage

### Single line

```powershell
python dia2_tts.py "[S1] Hello world, this is Dia2 TTS."
python dia2_tts.py "[S1] Hey! [S2] Hey yourself! [S1] (laughs) How are you?" --play
python dia2_tts.py "[S1] That was incredible." --out my_output.wav --seed 42
```

### Interactive mode

```powershell
python dia2_tts.py --interactive
```

Commands available in interactive mode:

| Command | Description |
|---|---|
| `/temp <value>` | Set audio sampling temperature |
| `/cfg <value>` | Set CFG scale |
| `/top-k <n>` | Set top-k sampling |
| `/seed <n>` | Fix random seed |
| `/noseed` | Return to random seed |
| `/play` / `/noplay` | Toggle immediate playback |
| `/prefix-s1 <path>` | Set speaker 1 voice prefix WAV |
| `/prefix-s2 <path>` | Set speaker 2 voice prefix WAV |
| `/noprefx` | Clear voice prefix |
| `/cuda-graph` / `/no-cuda-graph` | Toggle CUDA graph |
| `/quit` | Exit |

### Voice cloning

No transcript needed — Whisper handles it automatically.

```powershell
# Clone a single speaker
python dia2_tts.py "[S1] This is the generated speech." --prefix-s1 reference.wav

# Clone both speakers in a dialogue
python dia2_tts.py "[S1] Hello! [S2] Hey, how are you?" --prefix-s1 speaker1.wav --prefix-s2 speaker2.wav
```

### Model size

```powershell
# Default: Dia2-2B (~4 GB, better quality)
python dia2_tts.py "[S1] Hello."

# Faster: Dia2-1B (~2 GB)
python dia2_tts.py "[S1] Hello." --model nari-labs/Dia2-1B
```

---

## Dialogue Format

Dia2 is designed for dialogue. Always use speaker tags:

```
[S1] First speaker says this. [S2] Second speaker responds. [S1] Back to first speaker.
```

- Always start with `[S1]` (added automatically if omitted)
- Alternate between `[S1]` and `[S2]` — do not repeat the same speaker consecutively
- Supports up to ~2 minutes of generation

### Non-verbal tokens

| Token | Effect |
|---|---|
| `(laughs)` | Laughter |
| `(chuckle)` | Soft chuckle |
| `(sighs)` | Sigh |
| `(gasps)` | Gasp |
| `(coughs)` | Cough |
| `(sneezes)` | Sneeze |
| `(sniffs)` | Sniff |
| `(clears throat)` | Throat clearing |
| `(inhales)` | Audible inhale |
| `(exhales)` | Audible exhale |
| `(mumbles)` | Mumbling |
| `(humming)` | Humming |
| `(whistles)` | Whistling |
| `(singing)` | Singing |
| `(sings)` | Singing (alt) |
| `(groans)` | Groan |
| `(screams)` | Scream |
| `(claps)` | Clapping |
| `(applause)` | Applause |
| `(burps)` | Burp |
| `(beep)` | Beep sound |

Use sparingly — overusing or using unlisted non-verbals can cause audio artifacts.

---

## Parameters

| Flag | Default | Description |
|---|---|---|
| `--temp` | `0.8` | Audio sampling temperature. Lower = more stable (min ~0.5) |
| `--cfg-scale` | `2.0` | Classifier-free guidance scale (keep ≤ 3.0) |
| `--top-k` | `50` | Top-k sampling (replaces top-p from Dia1) |
| `--seed` | random | Fix seed for reproducible output |
| `--play` | off | Play audio immediately after generation |
| `--out` | auto | Custom output path |
| `--cuda-graph` | off | Enable CUDA graph for faster generation (no MSVC required) |
| `--model` | `Dia2-2B` | Model size: `nari-labs/Dia2-2B` or `nari-labs/Dia2-1B` |
| `--cpu` | off | Force CPU inference (very slow) |

---

## Troubleshooting

**CUDA out of memory**
Dia2-2B requires ~5 GB VRAM. Use `--model nari-labs/Dia2-1B` or close other GPU applications.

**Model download fails**
The model downloads from Hugging Face. Ensure a stable connection.
Caches to `~/.cache/huggingface/` and only downloads once.

**Whisper transcription takes a long time on first voice clone**
Whisper downloads its model the first time (~150 MB). Subsequent runs are faster.

**Audio sounds unnatural**
Try a longer / cleaner reference clip (5-10s, minimal background noise).

**`[S1]`/`[S2]` same speaker in a row**
Dia2 expects speakers to alternate. Avoid `[S1] ... [S1] ...` patterns.

**Empty audio / cfg_scale warning**
If `cfg_scale` is too high (> 3.0) or `temperature` too low (< 0.5), the model may not find
EOS and return silence. Stick to the safe ranges above.

---

## Credits

- [Dia2 TTS](https://github.com/nari-labs/dia2) by [Nari Labs](https://github.com/nari-labs)
- Models: [nari-labs/Dia2-2B](https://huggingface.co/nari-labs/Dia2-2B) · [nari-labs/Dia2-1B](https://huggingface.co/nari-labs/Dia2-1B)
- Auto-transcription via [whisper-timestamped](https://github.com/linto-ai/whisper-timestamped)

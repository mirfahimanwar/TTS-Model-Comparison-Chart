# Local TTS Model Comparison

Personal benchmark of open-source / local text-to-speech models.

**Hardware:** NVIDIA RTX 4090 Laptop GPU  
**Test prompt:** *"The quick brown fox jumped over the lazy dog. She laughed softly and said — well, that was unexpected. [sighs] I suppose we'll just have to try again."*

---

## Speed — Real-Time Factor (RTF)

> **RTF = Generation Time ÷ Audio Length**  
> RTF < 1.0 = faster than real-time | RTF = 1.0 = real-time | RTF > 1.0 = slower

| Model | 12s Time | 12s RTF | 30s Time | 30s RTF | 60s Time | 60s RTF | App Speed | CLI Speed |
|---|---|---|---|---|---|---|---|---|
| **Bark** | 16.4s | 1.33 | 42s | 1.35s | 81.4s | 1.37s | — | — |
| **Dia (Nari)** | 36s | 3.01 | — | — | — | — | 35s | — |
| **F5-TTS** | 4s | 0.33 | — | — | — | — | 4s | 14s |
| **Orpheus** | 12s | 1.00 | — | — | — | — | 12s | — |
| **Chatterbox** | 20s | 1.67 | — | — | — | — | 20s | — |
| **Coqui TTS** | 52s | 4.33 | — | — | — | — | 52s | — |
| **OpenVoice** | 19s | 1.58 | — | — | — | — | 19s | — |
| **Kyutai** | 12s | 1.00 | — | — | — | — | — | 12s |
| **Kyutai-Mimi** | 12s | 1.00 | — | — | — | — | — | 12s |
| **Higgs** | — | — | — | — | — | — | — | — |
| **Kokoro** | — | — | — | — | — | — | — | — |
| **XTTS** | — | — | — | — | — | — | — | — |
| **Sesame CSM** | — | — | — | — | — | — | — | — |
| **GPT-SoVITS** | — | — | — | — | — | — | — | — |
| **ChatTTS** | — | — | — | — | — | — | — | — |
| **IndexTTS2** | — | — | — | — | — | — | — | — |
| **Fish Speech** | — | — | — | — | — | — | — | — |
| **FireRedTTS** | — | — | — | — | — | — | — | — |
| **CosyVoice2** | — | — | — | — | — | — | — | — |
| **MaskGCT** | — | — | — | — | — | — | — | — |
| **Zonos** | — | — | — | — | — | — | — | — |
| **AllTalk TTS** | — | — | — | — | — | — | — | — |

> App Speed = measured in the model's own UI/webapp. CLI Speed = measured via command-line script.  
> `—` = not yet benchmarked. `❌` = could not get running.

---

## Quality Ratings

> All scores out of 5. Higher is better.  
> **Difficulty** = ease of install: 1 = one-click easy, 5 = failed to get running.

| Model | Emotions | Expressiveness | Consistency | No Trailing | Voice Cloning | Clone Quality | Difficulty |
|---|---|---|---|---|---|---|---|
| **Bark** | 4.0 | 2.5 | 2.0 | 2.5 | No | — | 1.0 |
| **Dia (Nari)** | 4.0 | 3.0 | 2.0 | 4.0 | Yes | 2.0 | 1.0 |
| **F5-TTS** | — | 3.0 | 4.5 | 5.0 | Yes | 4.5 | 2.0 |
| **Orpheus** | 2.5 | 2.5 | 5.0 | 3.0 | No | — | 2.0 |
| **Chatterbox** | — | 3.0 | 5.0 | 5.0 | Yes | 5.0 | 1.5 |
| **Coqui TTS** | 2.5 | 3.0 | 1.0 | 2.0 | Yes | 2.5 | 3.0 |
| **OpenVoice** | 1.0 | 2.0 | 3.5 | 2.0 | Yes | 2.0 | 2.0 |
| **Kyutai** | — | 4.0 | 5.0 | 5.0 | No | — | 3.0 |
| **Kyutai-Mimi** | — | 2.0 | 5.0 | 5.0 | Yes | 2.0 | 4.0 |
| **Higgs** | — | — | — | — | — | — | — |
| **Kokoro** | — | — | — | — | — | — | — |
| **XTTS** | — | — | — | — | — | — | — |
| **Sesame CSM** | — | — | — | — | — | — | 5.0 |
| **GPT-SoVITS** | — | — | — | — | — | — | 5.0 |
| **ChatTTS** | — | — | — | — | — | — | — |
| **IndexTTS2** | — | — | — | — | — | — | 5.0 |
| **Fish Speech** | — | — | — | — | — | — | — |
| **FireRedTTS** | — | — | — | — | — | — | — |
| **CosyVoice2** | — | — | — | — | — | — | — |
| **MaskGCT** | — | — | — | — | — | — | — |
| **Zonos** | — | — | — | — | — | — | — |
| **AllTalk TTS** | — | — | — | — | — | — | — |

**Column definitions:**
- **Emotions** — can it express different emotional tones (happy, sad, angry, etc.)
- **Expressiveness** — how natural and varied the delivery sounds
- **Consistency** — does the voice stay stable across multiple generations
- **Not Trailing** — does audio end cleanly without silence/noise at the end
- **Clone Quality** — how well it reproduces a reference voice (if supported)
- **Difficulty** — 1 = runs out of the box, 5 = could not get working

---

## Audio Samples

One male and one female sample per model, generated from the same test prompt.  
Click a link → GitHub opens the file page with an inline audio player.

| Model | Female | Male |
|---|---|---|
| **Bark** | [▶ female](samples/bark/female.wav) (en_speaker_9) | [▶ male](samples/bark/male.wav) (en_speaker_6) |
| **Dia (Nari)** | [▶ female](samples/dia/female.wav) | [▶ male](samples/dia/male.wav) |
| **F5-TTS** | [▶ female](samples/f5_tts/female.wav) | [▶ male](samples/f5_tts/male.wav) |
| **Orpheus** | [▶ female](samples/orpheus/female.wav) | [▶ male](samples/orpheus/male.wav) |
| **Chatterbox** | [▶ female](samples/chatterbox/female.wav) | [▶ male](samples/chatterbox/male.wav) |
| **Coqui TTS** | [▶ female](samples/coqui/female.wav) | [▶ male](samples/coqui/male.wav) |
| **OpenVoice** | [▶ female](samples/openvoice/female.wav) | [▶ male](samples/openvoice/male.wav) |
| **Kyutai** | [▶ female](samples/kyutai/female.wav) | [▶ male](samples/kyutai/male.wav) |
| **Kyutai-Mimi** | [▶ female](samples/kyutai_mimi/female.wav) | [▶ male](samples/kyutai_mimi/male.wav) |

---

## Model Repos

Each model lives in its own subfolder with a `setup.ps1` one-click installer and its own `venv/`.

| Model | Folder | Status |
|---|---|---|
| Bark | [BarkTTS/](BarkTTS/) | ✅ Ready |
| Dia (Nari) | [DiaTTS/](DiaTTS/) | — |
| F5-TTS | — | — |
| Orpheus | — | — |
| Chatterbox | — | — |
| Coqui TTS | — | — |
| OpenVoice | — | — |
| Kyutai | — | — |
| Kyutai-Mimi | — | — |

---

## Notes

- All benchmarks run on **NVIDIA RTX 4090 Laptop GPU** with models loaded fresh (no warm-up cache)
- RTF measured as wall-clock time from command submission to wav file written
- Quality scores are subjective — tested on the same 4–5 sentences per model
- `—` = not yet tested | `❌` = could not get running after reasonable effort
- 30s and 60s RTF columns will be filled in as each model is benchmarked

# Local TTS Model Comparison

Personal benchmark of open-source / local text-to-speech models.

**Hardware:** NVIDIA RTX 4090 Laptop GPU  
**Test prompt:** *"The quick brown fox jumped over the lazy dog. She laughed softly and said — well, that was unexpected. [sighs] I suppose we'll just have to try again."*

---

## Speed — Real-Time Factor (RTF)

> **RTF = Generation Time ÷ Audio Length**  
> RTF < 1.0 = faster than real-time | RTF = 1.0 = real-time | RTF > 1.0 = slower

| Model | 12s Time | 12s RTF | 30s Time | 30s RTF | 60s Time | 60s RTF | VRAM Usage | App Speed | CLI Speed |
|---|---|---|---|---|---|---|---|---|---|
| **Bark** | 16.4s | 1.33 | 42s | 1.35 | 81.4s | 1.37s |  | — | — |
| **Dia (Nari)** | 27.6 | 2.2 | 64.9s | 2.16 | — | — | — | 35s | — |
| **Dia2 (Nari)** | — | — | — | — | — | — | — | — | — |
| **F5-TTS** | 4s | 0.33 | — | — | — | — | — | 4s | 14s |
| **Orpheus - CLI** | 25.6s | 2.2 | 66.4s | 2.2 | — | — | 8.4 GB | 12s | — |
| **Orpheus** | 12s | 1.00 | — | — | — | — | — | 12s | — |
| **Chatterbox** | 24 | 1.67 | — | — | — | — | — | 20s | — |
| **Chatterbox - rsxdalv fast** | 6s | .5 | — | — | — | — | — | 20s | — |
| **Coqui TTS** | 52s | 4.33 | — | — | — | — | — | 52s | — |
| **OpenVoice** | 19s | 1.58 | — | — | — | — | — | 19s | — |
| **Kyutai** | 12s | 1.00 | — | — | — | — | — | — | 12s |
| **Kyutai-Mimi** | 12s | 1.00 | — | — | — | — | — | — | 12s |
| **Higgs** | — | — | — | — | — | — | — | — | — |
| **Kokoro** | — | — | — | — | — | — | — | — | — |
| **XTTS** | — | — | — | — | — | — | — | — | — |
| **Sesame CSM** | — | — | — | — | — | — | — | — | — |
| **GPT-SoVITS** | — | — | — | — | — | — | — | — | — |
| **ChatTTS** | — | — | — | — | — | — | — | — | — |
| **IndexTTS2** | — | — | — | — | — | — | — | — | — |
| **Fish Speech** | — | — | — | — | — | — | — | — | — |
| **FireRedTTS** | — | — | — | — | — | — | — | — | — |
| **CosyVoice2** | — | — | — | — | — | — | — | — | — |
| **MaskGCT** | — | — | — | — | — | — | — | — | — |
| **Zonos** | — | — | — | — | — | — | — | — | — |
| **AllTalk TTS** | — | — | — | — | — | — | — | — | — |
| **Qwen3-TTS** | — | — | — | — | — | — | — | — | — |
| **MegaTTS 3** | — | — | — | — | — | — | — | — | — |

> App Speed = measured in the model's own UI/webapp. CLI Speed = measured via command-line script.  
> `—` = not yet benchmarked. `❌` = could not get running.

---

## Quality Ratings

> All scores out of 5. Higher is better.  
> **Difficulty** = ease of install: 1 = one-click easy, 5 = failed to get running.

| Model | Emotions | Expressiveness | Consistency | No Trailing | No Cutoff | Realism | Voice Cloning | Clone Quality | Difficulty |
|---|---|---|---|---|---|---|---|---|---|
| **Bark** | 4.0 | 2.5 | 2.0 | 2.5 | 3.0 | — | No | — | 1.0 |
| **Dia (Nari)** | 4.0 | 3.0 | 2.0 | 4.0 | 3.0 | 3.5 | Yes | 2.5 | 1.0 |
| **Dia2 (Nari)** | 4.0 | 3.0 | 2.0 | 4.0 | 3.0 | 3.5 | Yes | 2.0 | 1.0 |
| **F5-TTS** | — | 3.0 | 4.5 | 5.0 | — | — | Yes | 4.5 | 2.0 |
| **Orpheus - CLI** | 2.0 | 3.0 | 4.0 | 4.5 | 4.5 | 4.0 | No | — | 1.0 |
| **Orpheus** | 2.5 | 2.5 | 4.0 | 3.0 | — | — | No | — | 2.0 |
| **Chatterbox** | — | 3.0 | 5.0 | 5.0 | — | — | Yes | 5.0 | 1.5 |
| **Coqui TTS** | 2.5 | 3.0 | 1.0 | 2.0 | — | — | Yes | 2.5 | 3.0 |
| **OpenVoice** | 1.0 | 2.0 | 3.5 | 2.0 | — | — | Yes | 2.0 | 2.0 |
| **Kyutai** | — | 4.0 | 5.0 | 5.0 | — | — | No | — | 3.0 |
| **Kyutai-Mimi** | — | 2.0 | 5.0 | 5.0 | — | — | Yes | 2.0 | 4.0 |
| **Higgs** | — | — | — | — | — | — | — | — | — |
| **Kokoro** | — | — | — | — | — | — | — | — | — |
| **XTTS** | — | — | — | — | — | — | — | — | — |
| **Sesame CSM** | — | — | — | — | — | — | — | — | 5.0 |
| **GPT-SoVITS** | — | — | — | — | — | — | — | — | 5.0 |
| **ChatTTS** | — | — | — | — | — | — | — | — | — |
| **IndexTTS2** | — | — | — | — | — | — | — | — | 5.0 |
| **Fish Speech** | — | — | — | — | — | — | — | — | — |
| **FireRedTTS** | — | — | — | — | — | — | — | — | — |
| **CosyVoice2** | — | — | — | — | — | — | — | — | — |
| **MaskGCT** | — | — | — | — | — | — | — | — | — |
| **Zonos** | — | — | — | — | — | — | — | — | — |
| **AllTalk TTS** | — | — | — | — | — | — | — | — | — |
| **Qwen3-TTS** | — | — | — | — | — | — | Yes | — | — |
| **MegaTTS 3** | — | — | — | — | — | — | Yes | — | — |

**Column definitions:**
- **Emotions** — can it express different emotional tones (happy, sad, angry, etc.)
- **Expressiveness** — how natural and varied the delivery sounds
- **Consistency** — does the voice stay stable across multiple generations
- **No Trailing** — does audio end cleanly without silence/noise after the speech
- **No Cutoff** — does speech complete fully without words being cut off at the end
- **Realism** — how human and lifelike the voice sounds (naturalness of prosody, breath, tone)
- **Voice Cloning** — supports cloning a voice from a reference audio file
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
| **Dia2 (Nari)** | — | — |
| **F5-TTS** | [▶ female](samples/f5_tts/female.wav) | [▶ male](samples/f5_tts/male.wav) |
| **Orpheus** | [▶ female](samples/orpheus/female.wav) | [▶ male](samples/orpheus/male.wav) |
| **Chatterbox** | [▶ female](samples/chatterbox/female.wav) | [▶ male](samples/chatterbox/male.wav) |
| **Coqui TTS** | [▶ female](samples/coqui/female.wav) | [▶ male](samples/coqui/male.wav) |
| **OpenVoice** | [▶ female](samples/openvoice/female.wav) | [▶ male](samples/openvoice/male.wav) |
| **Kyutai** | [▶ female](samples/kyutai/female.wav) | [▶ male](samples/kyutai/male.wav) |
| **Kyutai-Mimi** | [▶ female](samples/kyutai_mimi/female.wav) | [▶ male](samples/kyutai_mimi/male.wav) |
| **Higgs** | — | — |
| **Kokoro** | — | — |
| **XTTS** | — | — |
| **Sesame CSM** | — | — |
| **GPT-SoVITS** | — | — |
| **ChatTTS** | — | — |
| **IndexTTS2** | — | — |
| **Fish Speech** | — | — |
| **FireRedTTS** | — | — |
| **CosyVoice2** | — | — |
| **MaskGCT** | — | — |
| **Zonos** | — | — |
| **AllTalk TTS** | — | — |
| **Qwen3-TTS** | — | — |
| **MegaTTS 3** | — | — |

---

## Model Repos

Each model lives in its own subfolder with a `setup.ps1` one-click installer and its own `venv/`.

| Model | Folder | Status |
|---|---|---|
| Bark | [BarkTTS/](BarkTTS/) | ✅ Ready |
| Dia (Nari) | [DiaTTS/](DiaTTS/) | ✅ Ready |
| Dia2 (Nari) | [Dia2TTS/](Dia2TTS/) | ✅ Ready |
| F5-TTS | — | — |
| Orpheus | [Orpheus/](Orpheus/) | ✅ Ready (requires HF login — see Orpheus/README.md) |
| Chatterbox | [ChatterboxTTS/](ChatterboxTTS/) | ✅ Ready |
| Coqui TTS | — | — |
| OpenVoice | — | — |
| Kyutai | — | — |
| Kyutai-Mimi | — | — |
| Higgs | — | — |
| Kokoro | — | — |
| XTTS | — | — |
| Sesame CSM | — | — |
| GPT-SoVITS | — | — |
| ChatTTS | — | — |
| IndexTTS2 | — | — |
| Fish Speech S2 Pro | [FishAudioS2ProTTS/](FishAudioS2ProTTS/) | ✅ Ready |
| FireRedTTS | — | — |
| CosyVoice2 | — | — |
| MaskGCT | — | — |
| Zonos | — | — |
| AllTalk TTS | — | — |
| Qwen3-TTS | — | — |
| MegaTTS 3 | — | — |

**Community Recommended — Not Yet Benchmarked:**

| Model | Notes |
|---|---|
| MOSS-TTS | OpenMOSS-Team/MOSS-TTS — open weights, emotion control |
| HumeAI/tada | Cloud API only (requires account) |
| SoulX | Soul-AILab/SoulX — expressive, HuggingFace weights |
| VibeVoice | microsoft/VibeVoice |
| Neuphonic | neuphonic/neutts — cloud API only |
| Supertone-2 | Supertone/supertonic-2 |
| maya-research | Community recommendation, limited info |
| kittenTTS | Community recommendation, limited info |

---

## Notes

- All benchmarks run on **NVIDIA RTX 4090 Laptop GPU** with models loaded fresh (no warm-up cache)
- RTF measured as wall-clock time from command submission to wav file written
- Quality scores are subjective — tested on the same 4–5 sentences per model
- `—` = not yet tested | `❌` = could not get running after reasonable effort
- 30s and 60s RTF columns will be filled in as each model is benchmarked

---

## Expressive TTS — Emotion Tag Index

Which models support inline emotion tags that produce **real audio events** (not just prosody changes).

| Model | Emotion Tags | Tag Format | Sample Tags | VRAM | Voice Cloning |
|---|---|---|---|---|---|
| **Dia / Dia2** | ✅ 21 tags | `(laughs)` | `(laughs)` `(cries)` `(gasps)` `(sighs)` `(growls)` `(groans)` `(screams)` | 4–5 GB | ✅ |
| **Orpheus** | ✅ 8 tags | `<laugh>` | `<laugh>` `<sigh>` `<gasp>` `<groan>` `<cough>` `<sniffle>` `<yawn>` `<chuckle>` | 6–8 GB | ❌ |
| **Bark** | ⚠️ limited | `[laughter]` | `[laughter]` `[sighs]` `[clears throat]` | 6–8 GB | ❌ |
| **Fish Speech S2 Pro** | ⚠️ subtle | `[sighs]` | Tags present but produce mild prosody changes only | 14–15 GB | ✅ |
| **Higgs Audio v2** | ✅ emergent | none needed | Pass `instruct=` or embed emotion in text | 24 GB | ✅ |
| **Qwen3-TTS** | ✅ NL instructions | none needed | `instruct="speak with excitement"` | 3–8 GB | ✅ |
| **MegaTTS 3** | ❌ | none | No tag support — prosody via voice clone only | 8–16 GB | ✅ |
| **Chatterbox** | ❌ | none | Emotion via `exaggeration=` parameter (0.0–2.0) | 4–6 GB | ✅ |

### Best pick by use case

| Goal | Best Model | Why |
|---|---|---|
| Most emotion tags + local | **Dia2** | 21 tags, 4.4 GB, runs well on low VRAM |
| Laugh/cry/gasp audibly | **Orpheus** | Tags produce actual audio events, not just tone |
| No tags, emergent emotion | **Higgs Audio v2** | State-of-the-art EmergentTTS benchmark, 24 GB |
| NL-based emotion control | **Qwen3-TTS** | Natural language instruction, 3–8 GB |
| Voice clone + emotion | **Dia2** | Best combo of tags + clone quality at low VRAM |

### Dia tag list (21 total)

`(laughs)` `(chuckles)` `(giggles)` `(cries)` `(sobs)` `(sighs)` `(gasps)` `(screams)`  
`(moans)` `(groans)` `(growls)` `(sniffs)` `(yawns)` `(coughs)` `(clears throat)`  
`(whistles)` `(mumbles)` `(stutters)` `(hums)` `(shouts)` `(whispers)`

### Orpheus tag list (8 total)

`<laugh>` `<chuckle>` `<sigh>` `<cough>` `<sniffle>` `<groan>` `<yawn>` `<gasp>`

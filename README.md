# Local TTS Model Comparison

Personal benchmark of open-source / local text-to-speech models.

**Hardware:** NVIDIA RTX 4090 Laptop GPU  
**Test prompt:** *"The quick brown fox jumped over the lazy dog. She laughed softly and said — well, that was unexpected. [sighs] I suppose we'll just have to try again."*

---

## Model Reviews

Personal notes on each model after hands-on testing. 

---

### Bark

Although Bark natively doesn't support cloning, there is a 'bark with voice clone' repo that's included with this project. The voice cloning works, but isn't the best. The voice resembles the cloned one, but changes slightly every generation so it's not the most consistent. It can be fun, quirky, and expressive when you get lucky — but wildly inconsistent. As far as cloning goes the emotion tags (`[laughter]`, `[sighs]`) work sometimes and produce genuinely surprising results, but never quite know what you'll get. Voice cloning is limited; the `.npz` approach works but the clone just barely sounds close to the reference. It can also sometimes switch voices too, for example, if you clone a female voice, you may get a male voice, although rare in my testing, but still noteworthy to mention. Best used for creative/character TTS where some randomness is acceptable, not for production or narration work.

---

### Dia (Nari) — robertagee

The best emotion-tag model I've tested locally. Twenty-one tags that produce real audio events — laughs, cries, gasps, sighs, growls — not just tone shifts. Voice cloning via a reference transcript also works well. Slow at ~2.2× RTF, but the expressiveness payoff is worth it for short clips. Consistency is a weak spot; re-running the same text gives noticeably different deliveries.

---

### Dia2 (Nari)

Same architecture as Dia with similar quality. Slightly less reliable clone quality in my tests. Keeping both around to compare.

---

### F5-TTS

Fastest model in the lineup by a wide margin (RTF 0.33). Voice cloning is excellent — easily the best clone quality I've tested (4.5/5). No emotion tags, purely neutral TTS, but the voice reproduction is remarkably clean. Great pick when you need fast, high-quality cloned speech without any expressiveness requirements.

---

### Orpheus

Solid expressive model with eight clearly audible emotion tags via `<laugh>`, `<sigh>`, etc. The tags produce actual audio events, not just prosody shifts. Consistency is good (4.0/5) and realism is the highest I've rated at 4.0. No voice cloning support. CLI version is slower than the app version — worth measuring. Best choice when you want reliable, realistic delivery with light emotion control.

---

### Chatterbox

Shockingly clean output — perfect consistency (5.0/5) and no trailing noise or cutoffs. No emotion tags, but the `exaggeration=` parameter (0.0–2.0) pulls some range out of it. Clone quality is the best I've tested at 5.0/5. Fast rsxdalv variant brings it down to 0.5× RTF. The go-to model when quality and reliability matter more than expressiveness.

---

### VibeVoice

Interesting Microsoft research model — runs at nearly real-time (RTF ~0.93) and cloning works. Output is clean with minimal trailing issues. Not particularly expressive, but a solid all-rounder for neutral cloned speech. Marked as research-only so production use is uncertain.

---

### Coqui TTS

Very slow (RTF 4.33) and inconsistent quality. Cloning exists but the results aren't competitive with newer models. Fine for light local use but hard to recommend over anything else on this list given the speed.

---

### OpenVoice

Emotion control is weak (1.0/5) and clone quality is mediocre. Has trailing noise issues. Hasn't aged well — superseded by better cloning models. Keeping it benchmarked for historical reference.

---

### Kyutai

Excellent consistency (5.0/5) and very expressive (4.0/5). Runs at real-time (RTF 1.0). No voice cloning in the base model. Setup was moderately involved. One of the more impressive sounding models — wish it had clone support.

---

### Kyutai-Mimi

Same consistency as Kyutai but expressiveness drops to 2.0/5 in the Mimi variant. Clone support added but clone quality is poor (2.0/5). Notably harder to set up (difficulty 4.0). Mostly superseded by base Kyutai.

---

### Fish Speech S2 Pro

High VRAM (14–15 GB) but the voice cloning is very good and it supports a large number of speakers. Emotion tags are present but produce only subtle prosody changes. Worth running if you have the VRAM headroom and want a polished cloning experience.

---

### Higgs Audio v2

Haven't benchmarked yet. Emergent emotion control via `instruct=` parameter — no tags needed, just describe the emotion in natural language. 24 GB VRAM requirement is the main barrier. High ceiling on quality based on published benchmarks.

---

### Qwen3-TTS

Haven't benchmarked yet. NL-instruction emotion control — you describe the emotion in a separate instruction string. Flexible and interesting approach. Runs at 3–8 GB VRAM depending on the variant. Voice cloning supported.

---

### MegaTTS 3

Haven't benchmarked yet. No emotion tag support — prosody entirely from voice clone. High clone quality expected based on claims. 8–16 GB VRAM range.

---

### Kokoro, XTTS, Sesame CSM, GPT-SoVITS, ChatTTS, IndexTTS2, FireRedTTS, CosyVoice2, MaskGCT, Zonos, AllTalk TTS

Not yet tested.

---

## Speed — Real-Time Factor (RTF)

> **RTF = Generation Time ÷ Audio Length**  
> RTF < 1.0 = faster than real-time | RTF = 1.0 = real-time | RTF > 1.0 = slower

| Model | 12s Time | 12s RTF | 30s Time | 30s RTF | 60s Time | 60s RTF | VRAM Usage |
|---|---|---|---|---|---|---|---|
| **Bark** | 16.4s | 1.33 | 42s | 1.35 | 81.4s | 1.37s | 5.8 GB |
| **Dia (Nari) - robertagee** | 27.6s | 2.2 | 64.9s | 2.16 | — | — | — |
| **Dia2 (Nari)** | — | — | — | — | — | — | — |
| **F5-TTS** | 4s | 0.33 | — | — | — | — | — |
| **Orpheus - CLI** | 25.6s | 2.2 | 66.4s | 2.2 | — | — | 8.4 GB |
| **Orpheus** | 12s | 1.00 | — | — | — | — | — |
| **Chatterbox** | 24s | 1.67 | — | — | — | — | — |
| **Chatterbox - rsxdalv fast** | 6s | .5 | — | — | — | — | — |
| **VibeVoice** | 11s | .92 | 28.2s | .94 | 57s | .95 | 1.4 GB |
| **Coqui TTS** | 52s | 4.33 | — | — | — | — | — |
| **OpenVoice** | 19s | 1.58 | — | — | — | — | — |
| **Kyutai** | 12s | 1.00 | — | — | — | — | — |
| **Kyutai-Mimi** | 12s | 1.00 | — | — | — | — | — |
| **Higgs** | — | — | — | — | — | — | — |
| **Kokoro** | — | — | — | — | — | — | — |
| **XTTS** | — | — | — | — | — | — | — |
| **Sesame CSM** | — | — | — | — | — | — | — |
| **GPT-SoVITS** | — | — | — | — | — | — | — |
| **ChatTTS** | — | — | — | — | — | — | — |
| **IndexTTS2** | — | — | — | — | — | — | — |
| **Fish Speech** | — | — | — | — | — | — | — |
| **FireRedTTS** | — | — | — | — | — | — | — |
| **CosyVoice2** | — | — | — | — | — | — | — |
| **MaskGCT** | — | — | — | — | — | — | — |
| **Zonos** | — | — | — | — | — | — | — |
| **AllTalk TTS** | — | — | — | — | — | — | — |
| **Qwen3-TTS** | — | — | — | — | — | — | — |
| **MegaTTS 3** | — | — | — | — | — | — | — |

> `—` = not yet benchmarked. `❌` = could not get running.

---

## Quality Ratings

> All scores out of 5. Higher is better.  
> **Difficulty** = ease of install: 1 = one-click easy, 5 = failed to get running.

| Model | Emotion Tags | Emotions | Expressiveness | Consistency | No Trailing | No Cutoff | Realism | Voice Cloning | Clone Quality | Difficulty |
|---|---|---|---|---|---|---|---|---|---|---|
| **Bark** | Yes | 4.0 | 2.5 | 2.0 | 2.5 | 3.0 | — | Yes | — | 1.0 |
| **Dia (Nari)** | Yes | 4.0 | 3.0 | 2.0 | 4.0 | 3.0 | 3.5 | Yes | 2.5 | 1.0 |
| **Dia2 (Nari)** | Yes | 4.0 | 3.0 | 2.0 | 4.0 | 3.0 | 3.5 | Yes | 2.0 | 1.0 |
| **F5-TTS** | No | — | 3.0 | 4.5 | 5.0 | — | — | Yes | 4.5 | 2.0 |
| **Orpheus - CLI** | Yes | 2.0 | 3.0 | 4.0 | 4.5 | 4.5 | 4.0 | No | — | 1.0 |
| **Orpheus** | Yes | 2.5 | 2.5 | 4.0 | 3.0 | — | — | No | — | 2.0 |
| **Chatterbox** | No | — | 3.0 | 5.0 | 5.0 | — | — | Yes | 5.0 | 1.5 |
| **VibeVoice** | No | 0 | 2.0 | 3.5 | 4.5 | 4.5 | 2.0 | Yes | 3.5 | 1.0 |
| **Coqui TTS** | — | 2.5 | 3.0 | 1.0 | 2.0 | — | — | Yes | 2.5 | 3.0 |
| **OpenVoice** | — | 1.0 | 2.0 | 3.5 | 2.0 | — | — | Yes | 2.0 | 2.0 |
| **Kyutai** | — | — | 4.0 | 5.0 | 5.0 | — | — | No | — | 3.0 |
| **Kyutai-Mimi** | — | — | 2.0 | 5.0 | 5.0 | — | — | Yes | 2.0 | 4.0 |
| **Higgs** | — | — | — | — | — | — | — | — | — | — |
| **Kokoro** | — | — | — | — | — | — | — | — | — | — |
| **XTTS** | — | — | — | — | — | — | — | — | — | — |
| **Sesame CSM** | — | — | — | — | — | — | — | — | — | 5.0 |
| **GPT-SoVITS** | — | — | — | — | — | — | — | — | — | 5.0 |
| **ChatTTS** | — | — | — | — | — | — | — | — | — | — |
| **IndexTTS2** | — | — | — | — | — | — | — | — | — | 5.0 |
| **Fish Speech** | — | — | — | — | — | — | — | — | — | — |
| **FireRedTTS** | — | — | — | — | — | — | — | — | — | — |
| **CosyVoice2** | — | — | — | — | — | — | — | — | — | — |
| **MaskGCT** | — | — | — | — | — | — | — | — | — | — |
| **Zonos** | — | — | — | — | — | — | — | — | — | — |
| **AllTalk TTS** | — | — | — | — | — | — | — | — | — | — |
| **Qwen3-TTS** | — | — | — | — | — | — | — | Yes | — | — |
| **MegaTTS 3** | — | — | — | — | — | — | — | Yes | — | — |

**Column definitions:**
- **Emotion Tags** — supports emotion/tone markup tags in input text (e.g. `[laughs]`, `(whispers)`, `<happy>`)
- **Emotions** — can it express different emotional tones via tags (happy, sad, angry, etc.)
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
| **VibeVoice** | — | — |

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
| VibeVoice | [VibeVoiceTTS/](VibeVoiceTTS/) | ✅ Ready (research only — see VibeVoiceTTS/README.md) |
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
| ~~VibeVoice~~ | ~~microsoft/VibeVoice~~ — now in [VibeVoiceTTS/](VibeVoiceTTS/) |
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

# Local TTS Model Comparison

Personal benchmark of open-source / local text-to-speech models.

**Hardware:** NVIDIA RTX 4090 Laptop GPU  
**Test prompt:** *"The quick brown fox jumped over the lazy dog. She laughed softly and said — well, that was unexpected. [sighs] I suppose we'll just have to try again."*

---

## Model Reviews

Personal notes on each model after hands-on testing. Real Time Factor (RTF) refers to Generation Time divided by Generated Audio Time. I.E: If it takes 60 seconds to generate 30 seconds of audio, its RTF would be 2. The lower the RTF the faster the response.

---

### Bark

Although the main Bark repo doesn't natively support voice cloning itself, there is a 'bark-with-voice-clone' repo that I included with the one click installer. The voice cloning does work, but it isn't the best. The voice does somewhat resemble the cloned one, but changes slightly every generation so it's not the most consistent - almost as if you varied your own voice everytime you talk, but with a different starting voice. Anyways, It can be fun, quirky, and expressive when you get lucky — but oftentimes inconsistent. As far as voice cloning goes - the emotion tags (`[laughter]`, `[sighs]`, etc.) work sometimes and can produce surprising results, but you never quite know what you'll get. Sometimes (with voice cloning) it may skip emotion tags entirely. I will say though, it's kinda impressive it can take a voice (without laughing, sighing, etc) and relatively apply those emotions to a voice that wasn't trained on it. Voice cloning is limited; the `.npz` approach works but the clone just barely sounds close to the reference. It can also sometimes switch voices too, for example, if you clone a female voice, you may get a male voice, although rare in my testing, but still noteworthy to mention. Otherwise, it isn't really that expressive. It sounds almost half robotic and half human. It does work a little better without voice cloning though, if you don't mind the presest voices, which there's quite a few of. Best used for creative/character TTS where some randomness is acceptable, not for production, narration work, or voice assistants. It's also not the fastest, nor the slowest either with 1.35 RTF. Note: Although the official repository seems to use brackets for emotions tags, I've found that parenthesis seem to be better. Using the brackets increases the chances it'll sound less like the voice clone and vary the voice more. The voice cloning also increases the RTF from 1.35 to about 1.43 as well. Longer sentences can increase the likelihood that the voice deviates, but there is a --rolling flag that I added in you can use - meaning - it should use the context of the voice prior to the chunking, but this doesn't always work the best. There is also a pre-existing --seed flag you can use as well which allows you to use the seed you liked for reproducability to mitigate these issues. Voices are more consistent if don't use voice cloning.

---

### Dia — robertagee

This is the best emotion-tag model I've tested locally. Twenty-one tags that produce real audio events — laughs, gasps, sighs, etc.  — not just tone shifts. Some of the tags don't work that well with voice cloning, however. The one's that don't work as well have already been tested and are listed in the main one click installer repo I created. Voice cloning via a reference transcript also works well. It can be slow at ~2.2× RTF, but the expressiveness payoff is worth it for short clips as well as the decent clone quality. Consistency is pretty solid as well.. It's not the best, but it does sound like the cloned voice, and keeps it's likeness throughout generations (although does vary slightly). If you want it to be faster, you can use the --compile flag which uses torch.compile to optimize. This brings RTF down to a whopping .77! Faster than real time! Although that doesn't mean it responds right away, it just means that the audio takes less time to generate than the clip is long. The expressiveness is very advanced. Almost too advanced. By that, I mean, it almost takes away it's human likeness because it's too expressive at times. But if you want a fun, expressive voice, then this is a great model to use. If this model was paired with the speed of Kokoro it'd be very hard to beat. Then if you added F5's voice cloning ability, and it would become SOTA in my opinion.

---

### Dia2

Actually way worse than Dia. Not sure why. I even installed Triton and it uses Cuda-Graph too. I messed around a long time with this one to see if Claude Opus 4.5 could optimize it, but it's RTF was about 3.7 at best. Significantly less reliable clone quality in my tests too.

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
| **Bark (Voice Clone)** | 16.9s | 1.41 | 42.9s | 1.43 | 85.2s | 1.42s | 5.8 GB |
| **Dia - robertagee** | 27.6s | 2.2 | 64.9s | 2.16 | — | — | — |
| **Dia (Voice Clone) - robertagee** | 27.6s | 2.2 | 64.9s | 2.16 | — | — | — |
| **Dia - (Voice Clone) - robertagee (--compile)** | 9.4s | **0.77** | 23.1s | **0.77** | 47s | **0.78** | 6.2 GB |
| **Dia2** | 44.4 | 3.7 | — | — | — | — | — |
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

| Model | Emotion Tags | Emotions | Expressiveness | Consistency | No Artifacts | No Trailing | No Cutoff | Realism | Voice Cloning | Clone Quality | Difficulty |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Bark** | Yes | 3.0 | 2.5 | 3.5 | 3.0 | 4.5 | 4.5 | 2.5 | No | — | 1.0 |
| **Bark (Voice Clone)** | Yes | 2.5 | 2.0 | 2.0 | 3.0 | 4.5 | 4.5 | 2.5 | Yes | 1.5 | 1.0 |
| **Dia** | Yes | 4.0 | 3.0 | 2.0 | — | 4.0 | 3.0 | 3.5 | Yes | 2.5 | 1.0 |
| **Dia (Voice Clone) - robertagee** | Yes | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | 3.5 | 3.5 | Yes | 3.5 | 1.0 |
| **Dia (Voice Clone) - robertagee (--compile)** | Yes | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | 4.0 | Yes | 3.5 | 1.0 |
| **Dia2** | Yes | 1.0 | 2.0 | 2.0 | 0.5 | 2.0 | 3.0 | 0.5 | Yes | 0.0 | 4.0 |
| **F5-TTS** | No | — | 3.0 | 4.5 | — | 5.0 | — | — | Yes | 4.5 | 2.0 |
| **Orpheus - CLI** | Yes | 2.0 | 3.0 | 4.0 | — | 4.5 | 4.5 | 4.0 | No | — | 1.0 |
| **Orpheus** | Yes | 2.5 | 2.5 | 4.0 | — | 3.0 | — | — | No | — | 2.0 |
| **Chatterbox** | No | — | 3.0 | 5.0 | — | 5.0 | — | — | Yes | 5.0 | 1.5 |
| **VibeVoice** | No | 0 | 2.0 | 3.5 | — | 4.5 | 4.5 | 2.0 | Yes | 3.5 | 1.0 |
| **Coqui TTS** | — | 2.5 | 3.0 | 1.0 | — | 2.0 | — | — | Yes | 2.5 | 3.0 |
| **OpenVoice** | — | 1.0 | 2.0 | 3.5 | — | 2.0 | — | — | Yes | 2.0 | 2.0 |
| **Kyutai** | — | — | 4.0 | 5.0 | — | 5.0 | — | — | No | — | 3.0 |
| **Kyutai-Mimi** | — | — | 2.0 | 5.0 | — | 5.0 | — | — | Yes | 2.0 | 4.0 |
| **Higgs** | — | — | — | — | — | — | — | — | — | — | — |
| **Kokoro** | — | — | — | — | — | — | — | — | — | — | — |
| **XTTS** | — | — | — | — | — | — | — | — | — | — | — |
| **Sesame CSM** | — | — | — | — | — | — | — | — | — | — | 5.0 |
| **GPT-SoVITS** | — | — | — | — | — | — | — | — | — | — | 5.0 |
| **ChatTTS** | — | — | — | — | — | — | — | — | — | — | — |
| **IndexTTS2** | — | — | — | — | — | — | — | — | — | — | 5.0 |
| **Fish Speech** | — | — | — | — | — | — | — | — | — | — | — |
| **FireRedTTS** | — | — | — | — | — | — | — | — | — | — | — |
| **CosyVoice2** | — | — | — | — | — | — | — | — | — | — | — |
| **MaskGCT** | — | — | — | — | — | — | — | — | — | — | — |
| **Zonos** | — | — | — | — | — | — | — | — | — | — | — |
| **AllTalk TTS** | — | — | — | — | — | — | — | — | — | — | — |
| **Qwen3-TTS** | — | — | — | — | — | — | — | — | Yes | — | — |
| **MegaTTS 3** | — | — | — | — | — | — | — | — | Yes | — | — |

**Column definitions:**
- **Emotion Tags** — supports emotion/tone markup tags in input text (e.g. `[laughs]`, `(whispers)`, `<happy>`)
- **Emotions** — how well and consistent it can express different emotional tones via tags (happy, sad, angry, etc.)
- **Expressiveness** — how natural and varied the delivery sounds
- **Consistency** — does the voice stay stable and consistent across multiple generations
- **No Artifacts** — absence of digital glitches, clicks, static, distortion, or unnatural audio discontinuities mid-speech
- **No Trailing** — does audio end cleanly without silence/noise or random noise after the speech
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
| **Dia** | [▶ female](samples/dia/female.wav) | [▶ male](samples/dia/male.wav) |
| **Dia2** | — | — |
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

| Model | Status | GitHub |
|---|---|---|
| Bark | ✅ Ready | [Bark_TTS_CLI_Local](https://github.com/mirfahimanwar/Bark_TTS_CLI_Local) |
| Dia | ✅ Ready | [Dia-TTS-CLI-Local](https://github.com/mirfahimanwar/Dia-TTS-CLI-Local) |
| Dia2 | ✅ Ready | [Dia-2-TTS-CLI-Local](https://github.com/mirfahimanwar/Dia-2-TTS-CLI-Local) |
| F5-TTS | — | — |
| Orpheus | ✅ Ready (requires HF login) | [Orpheus-TTS-CLI-Local](https://github.com/mirfahimanwar/Orpheus-TTS-CLI-Local) |
| Chatterbox | ✅ Ready | [Chatterbox-TTS-CLI-Local](https://github.com/mirfahimanwar/Chatterbox-TTS-CLI-Local) |
| VibeVoice | ✅ Ready (research only) | — |
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
| Fish Speech S2 Pro | ✅ Ready | — |
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

# setup.ps1 -- One-click Windows setup for Dia2TTS
# Run from the Dia2TTS folder:
#   .\setup.ps1
#
# What it does:
#   1. Clones nari-labs/dia2 into dia2/
#   2. Creates a Python virtual environment
#   3. Installs PyTorch with CUDA 12.8
#   4. Installs dia2 and all dependencies
#   5. Installs sounddevice for --play support
#
# Requirements:
#   - Python 3.10+
#   - Git
#   - NVIDIA GPU + CUDA 12.8 drivers (nvidia-smi should show CUDA 12.8)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$ROOT = $PSScriptRoot

# ── 1. Clone dia2 repo ────────────────────────────────────────────────────────
if (Test-Path "$ROOT\dia2\.git") {
    Write-Host "[1/5] dia2/ already cloned -- skipping" -ForegroundColor Cyan
} else {
    Write-Host "[1/5] Cloning nari-labs/dia2..." -ForegroundColor Cyan
    git clone https://github.com/nari-labs/dia2 "$ROOT\dia2"
    if ($LASTEXITCODE -ne 0) { throw "git clone failed" }
}

# ── 2. Create venv ────────────────────────────────────────────────────────────
if (Test-Path "$ROOT\venv\Scripts\python.exe") {
    Write-Host "[2/5] venv already exists -- skipping" -ForegroundColor Cyan
} else {
    Write-Host "[2/5] Creating virtual environment..." -ForegroundColor Cyan
    python -m venv "$ROOT\venv"
    if ($LASTEXITCODE -ne 0) { throw "venv creation failed" }
}

$PIP = "$ROOT\venv\Scripts\pip.exe"
$PYTHON = "$ROOT\venv\Scripts\python.exe"

# ── 3. Install PyTorch with CUDA 12.8 ─────────────────────────────────────────
# dia2 requires torch>=2.8.0. Install from the cu128 index first so the CUDA
# build is selected. PyPI would otherwise install a CPU-only build.
Write-Host "[3/5] Installing PyTorch (CUDA 12.8)..." -ForegroundColor Cyan
& $PIP install torch torchaudio --index-url https://download.pytorch.org/whl/cu128
if ($LASTEXITCODE -ne 0) { throw "PyTorch install failed" }

# ── 4. Install dia2 and dependencies ─────────────────────────────────────────
# Install deps explicitly first (pyproject.toml uses uv format which pip may
# not fully resolve), then install dia2 in editable mode.
Write-Host "[4/5] Installing dia2 dependencies..." -ForegroundColor Cyan
& $PIP install `
    "numpy>=2.1.0,<3.0" `
    "transformers>=4.55.3" `
    "safetensors==0.5.3" `
    "huggingface-hub>=0.24.7" `
    "sphn>=0.2.0" `
    "soundfile>=0.12.1" `
    "whisper-timestamped>=1.14.2" `
    "gradio>=4.44.1" `
    --extra-index-url https://download.pytorch.org/whl/cu128
if ($LASTEXITCODE -ne 0) { throw "dependency install failed" }

Write-Host "[4/5] Installing dia2 (editable)..." -ForegroundColor Cyan
& $PIP install -e "$ROOT\dia2" --no-deps
if ($LASTEXITCODE -ne 0) { throw "dia2 install failed" }

# ── 5. Install extras ─────────────────────────────────────────────────────────
Write-Host "[5/5] Installing extras (sounddevice)..." -ForegroundColor Cyan
& $PIP install sounddevice
if ($LASTEXITCODE -ne 0) { throw "extras install failed" }

# ── Done ──────────────────────────────────────────────────────────────────────
Write-Host ""
Write-Host "Setup complete!" -ForegroundColor Green
Write-Host ""

# Activate the venv in the current shell (only works when dot-sourced: . .\setup.ps1)
. "$ROOT\venv\Scripts\Activate.ps1"
Write-Host "Venv activated." -ForegroundColor Green
Write-Host ""
Write-Host "Quick start:" -ForegroundColor Yellow
Write-Host '  python dia2_tts.py "[S1] Hello world, this is Dia2 TTS."'
Write-Host '  python dia2_tts.py "[S1] Hey! [S2] Hey yourself! [S1] (laughs)" --play'
Write-Host '  python dia2_tts.py --interactive'
Write-Host ""
Write-Host "Voice cloning (no transcript needed -- Whisper auto-transcribes):" -ForegroundColor Yellow
Write-Host '  python dia2_tts.py "[S1] Hello." --prefix-s1 reference.wav'
Write-Host ""
Write-Host "Note: First run downloads the model from Hugging Face." -ForegroundColor DarkGray
Write-Host "  Dia2-2B (default): ~4 GB" -ForegroundColor DarkGray
Write-Host "  Dia2-1B (faster):  ~2 GB  (pass --model nari-labs/Dia2-1B)" -ForegroundColor DarkGray

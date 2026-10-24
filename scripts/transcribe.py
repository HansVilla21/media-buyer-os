"""Transcribe a course video on this machine with faster-whisper.

Usage (from the project root):
    .venv/Scripts/python.exe scripts/transcribe.py <video.mp4> <out_dir>
        [--model large-v3] [--device cuda|cpu] [--compute-type float16]
        [--language es]        # omit to auto-detect on the first 30 s of speech
        [--sample-minutes N]   # transcribe only the first N minutes (quality/speed check)

Output: <out_dir>/transcripcion.md    paragraphs, each with its start timestamp
        <out_dir>/transcripcion.json  every segment with timing and confidence (lossless form)

Audio is extracted with ffmpeg to a temporary 16 kHz mono WAV under .cache/tmp. Models are
cached in .cache/models, so nothing is installed outside the project.
"""

from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_CACHE = PROJECT_ROOT / ".cache" / "models"
TMP_DIR = PROJECT_ROOT / ".cache" / "tmp"
PARAGRAPH_MAX_SECONDS = 45.0
PARAGRAPH_GAP_SECONDS = 1.5
# Vocabulary the course uses (Spanish speech with English trade terms); biases the decoder so
# "Media Buying" does not come out as "Miriam Bain".
HOTWORDS = ("Media Buying, Media Buyer, Media Buyers HQ, Facebook Ads, Meta, Instagram, Business Manager, "
            "Ads Manager, leads, lead, nicho, avatar, oferta, copy, ad, ads, video ad, funnel, setter, closer, "
            "CPM, CTR, CPL, CPA, ROAS, ROI, pixel, campaña, conjunto de anuncios, presupuesto, escalar, "
            "testimonios, mecanismo, ángulo, llamado a la acción, WhatsApp, Skool, ChatGPT")


def register_cuda_dlls() -> None:
    """Make the pip-installed cuBLAS/cuDNN DLLs visible to CTranslate2 (Windows)."""
    for package in ("nvidia.cublas", "nvidia.cudnn"):
        spec = importlib.util.find_spec(package)
        if not spec or not spec.submodule_search_locations:
            continue
        for location in spec.submodule_search_locations:
            bin_dir = Path(location) / "bin"
            if bin_dir.is_dir():
                os.environ["PATH"] = f"{bin_dir}{os.pathsep}{os.environ.get('PATH', '')}"
                if hasattr(os, "add_dll_directory"):
                    os.add_dll_directory(str(bin_dir))


def probe_duration(video: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(video)],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return float(out)


def extract_audio(video: Path, wav: Path, sample_minutes: float | None) -> None:
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(video)]
    if sample_minutes:
        cmd += ["-t", str(sample_minutes * 60)]
    cmd += ["-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(wav)]
    subprocess.run(cmd, check=True)


def load_wav(wav: Path):
    """Read the 16 kHz mono PCM WAV as float32 samples (avoids faster-whisper's PyAV decoding)."""
    import wave

    import numpy as np

    with wave.open(str(wav), "rb") as handle:
        assert handle.getnchannels() == 1 and handle.getframerate() == 16000 and handle.getsampwidth() == 2
        frames = handle.readframes(handle.getnframes())
    return np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0


def hms(seconds: float) -> str:
    total = int(seconds)
    return f"{total // 3600}:{total % 3600 // 60:02d}:{total % 60:02d}"


def paragraphs(segments: list[dict]) -> list[tuple[float, str]]:
    """Group segments into paragraphs: a new one after a long pause or every ~45 s."""
    result: list[tuple[float, str]] = []
    current_start: float | None = None
    current_text: list[str] = []
    last_end: float | None = None
    for seg in segments:
        text = seg["text"].strip()
        if not text:
            continue
        starts_new = (
            current_start is None
            or (last_end is not None and seg["start"] - last_end > PARAGRAPH_GAP_SECONDS)
            or seg["end"] - current_start > PARAGRAPH_MAX_SECONDS
        )
        if starts_new:
            if current_text:
                result.append((current_start, " ".join(current_text)))
            current_start, current_text = seg["start"], []
        current_text.append(text)
        last_end = seg["end"]
    if current_text:
        result.append((current_start, " ".join(current_text)))
    return result


def write_outputs(out_dir: Path, video: Path, args: argparse.Namespace, info, segments: list[dict],
                  duration: float, elapsed: float) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    transcribed_at = dt.datetime.now().isoformat(timespec="seconds")
    meta = {
        "video": str(video),
        "video_duration_seconds": round(duration, 1),
        "transcribed_seconds": round(min(duration, args.sample_minutes * 60), 1) if args.sample_minutes else round(duration, 1),
        "model": args.model,
        "compute_type": args.compute_type,
        "batch_size": args.batch_size,
        "language": info.language,
        "language_probability": round(info.language_probability, 3),
        "transcribed_at": transcribed_at,
        "elapsed_seconds": round(elapsed, 1),
        "segments": segments,
    }
    (out_dir / "transcripcion.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")

    sample_note = f" (muestra: primeros {args.sample_minutes:g} min)" if args.sample_minutes else ""
    lines = [
        f"# Transcripción — {video.name}",
        "",
        f"- Video: `{video}`",
        f"- Duración: {hms(duration)}{sample_note}",
        f"- Modelo: {args.model} ({args.compute_type}) · idioma: {info.language} ({info.language_probability:.2f})",
        f"- Transcrito: {transcribed_at}, en {hms(elapsed)}",
        "",
        "Transcripción automática: puede tener errores en nombres y cifras. Ante la duda, el video manda.",
        "",
        "---",
        "",
    ]
    for start, text in paragraphs(segments):
        lines.append(f"**[{hms(start)}]** {text}")
        lines.append("")
    (out_dir / "transcripcion.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("video", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--model", default="large-v3")
    parser.add_argument("--device", default="cuda")
    # int8 weights: fits the 6 GB GPU with batching and runs ~6x real time there (float16 ran
    # out of memory on a full session and was 3x slower)
    parser.add_argument("--compute-type", default="int8_float16")
    parser.add_argument("--language", default=None)
    parser.add_argument("--sample-minutes", type=float, default=None)
    parser.add_argument("--batch-size", type=int, default=4,
                        help="batched decoding of VAD chunks (much faster on GPU); 0 = sequential")
    parser.add_argument("--hotwords", default=HOTWORDS, help="vocabulary to bias recognition; '' disables it")
    args = parser.parse_args()

    register_cuda_dlls()
    from faster_whisper import BatchedInferencePipeline, WhisperModel  # after the DLLs are registered

    duration = probe_duration(args.video)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=TMP_DIR) as tmp:
        wav = Path(tmp) / "audio.wav"
        print(f"extracting audio ({hms(duration)}) ...", file=sys.stderr, flush=True)
        extract_audio(args.video, wav, args.sample_minutes)

        print(f"loading {args.model} on {args.device}/{args.compute_type} ...", file=sys.stderr, flush=True)
        model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type,
                             download_root=str(MODEL_CACHE))

        audio = load_wav(wav)
        started = time.time()
        options = {
            "language": args.language,
            "beam_size": 5,
            "vad_filter": True,
            "vad_parameters": {"min_silence_duration_ms": 500},
            # each window is decoded on its own: avoids the repetition loops and the
            # punctuation drift that conditioning on previous text causes in long recordings
            "condition_on_previous_text": False,
            "hotwords": args.hotwords or None,
        }
        if args.batch_size > 0:
            segment_iter, info = BatchedInferencePipeline(model=model).transcribe(
                audio, batch_size=args.batch_size, **options)
        else:
            segment_iter, info = model.transcribe(audio, **options)
        print(f"language: {info.language} ({info.language_probability:.2f})", file=sys.stderr, flush=True)
        segments: list[dict] = []
        for seg in segment_iter:
            segments.append({
                "start": round(seg.start, 2),
                "end": round(seg.end, 2),
                "text": seg.text.strip(),
                "avg_logprob": round(seg.avg_logprob, 3),
                "no_speech_prob": round(seg.no_speech_prob, 3),
            })
            if len(segments) % 100 == 0:
                print(f"  {hms(seg.end)} done, {time.time() - started:.0f}s elapsed", file=sys.stderr, flush=True)
        elapsed = time.time() - started

    write_outputs(args.out_dir, args.video, args, info, segments, duration, elapsed)
    print(f"done: {len(segments)} segments in {hms(elapsed)} -> {args.out_dir}", file=sys.stderr, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

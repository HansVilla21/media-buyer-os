#!/usr/bin/env bash
# Transcribe every course session that is not transcribed yet, one after another (one GPU),
# and convert each session's resources on the way. Safe to re-run: finished sessions are skipped.
#
# Usage (from the project root, Git Bash):
#     bash scripts/transcribe_queue.sh
# Log: .cache/transcribe-queue.log

set -u -o pipefail
cd "$(dirname "$0")/.."
export HF_HUB_DISABLE_SYMLINKS_WARNING=1
PY=".venv/Scripts/python.exe"
SRC="C:/Users/hvill/Downloads/Media Buyer HQ"
LOG=".cache/transcribe-queue.log"
mkdir -p .cache

# session number | source folder | video file | destination folder
QUEUE="
3|Sesion 3|sesion-3-cosmic-ai-copywriting.mp4|sesion-03-cosmic-ai-copywriting
4|Sesion 4|sesion-4-video-ad-alchemy.mp4|sesion-04-video-ad-alchemy
5|Sesion 5|sesion-5-fusion-funnels.mp4|sesion-05-fusion-funnels
6|Sesion 6|sesion-6-ad-campaign-ignition.mp4|sesion-06-ad-campaign-ignition
7|Sesion 7|sesion-7-meta-business-manager.mp4|sesion-07-meta-business-manager
8|Sesion 8|sesion-8-algorithmic-targeting.mp4|sesion-08-algorithmic-targeting
9|Sesion 9|sesion-9-key-metrics.mp4|sesion-09-key-metrics
17|Sesion 17|sesion-10-media-buyer-delivery.mp4|sesion-17-media-buyer-delivery
18|Sesion 18|sesion-18.mp4|sesion-18-clientes-para-el-servicio
"

# The queue is read on descriptor 3 and every child gets stdin from /dev/null: otherwise the
# transcriber swallows the remaining queue lines as its own input and sessions get skipped.
while IFS='|' read -r -u 3 number folder video dest; do
  [ -z "$number" ] && continue
  out="inputs/curso/$dest"
  if [ ! -f "$out/fuente.md" ]; then
    echo "[$(date +%H:%M:%S)] resources: session $number" | tee -a "$LOG"
    "$PY" scripts/convert_resources.py "$SRC/$folder" "$out" --session "$number" >>"$LOG" 2>&1 </dev/null
  fi
  if [ -f "$out/transcripcion.json" ]; then
    echo "[$(date +%H:%M:%S)] skip: session $number already transcribed" | tee -a "$LOG"
    continue
  fi
  echo "[$(date +%H:%M:%S)] transcribing: session $number ($video)" | tee -a "$LOG"
  if "$PY" scripts/transcribe.py "$SRC/$folder/$video" "$out" --model large-v3 --language es \
       --compute-type int8_float16 --batch-size 4 >>"$LOG" 2>&1 </dev/null; then
    echo "[$(date +%H:%M:%S)] done: session $number" | tee -a "$LOG"
  else
    echo "[$(date +%H:%M:%S)] FAILED: session $number (see $LOG)" | tee -a "$LOG"
  fi
done 3< <(printf '%s\n' "$QUEUE" | grep -v '^\s*$')
echo "[$(date +%H:%M:%S)] queue finished" | tee -a "$LOG"

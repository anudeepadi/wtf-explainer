#!/usr/bin/env bash
# One frame every 4 seconds (keyframes only, fast), 480px wide. Frame N ≈ (N-1)*4 seconds.
set -euo pipefail
for v in vid/*.mp4; do
  n=$(basename "$v" .mp4); mkdir -p "frames/$n"
  ffmpeg -nostdin -loglevel error -skip_frame nokey -i "$v" -vf 'fps=1/4,scale=480:-2' -q:v 4 "frames/$n/f_%05d.jpg"
  echo "$n: $(ls "frames/$n" | wc -l) frames"
done

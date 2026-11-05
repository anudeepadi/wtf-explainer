#!/usr/bin/env bash
# Download timestamped captions (json3) + a 360p copy of each episode for local analysis.
# Usage: ./01_fetch.sh picks.txt   (needs yt-dlp + ffmpeg; run on a normal home connection)
set -euo pipefail
PICKS=${1:-picks.txt}
mkdir -p subs vid
grep -v '^#' "$PICKS" | while read -r id name; do
  [ -z "$id" ] && continue
  yt-dlp -q --skip-download --write-auto-subs --write-subs --sub-langs "en.*,en" \
    --sub-format json3 --write-info-json -o "subs/$name.%(ext)s" "https://www.youtube.com/watch?v=$id" || true
  [ -f "vid/$name.mp4" ] || yt-dlp -q -f 'bv*[height<=360][ext=mp4]/bv*[height<=360]/worst' \
    --remux-video mp4 -o "vid/$name.%(ext)s" "https://www.youtube.com/watch?v=$id"
done

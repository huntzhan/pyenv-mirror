#!/usr/bin/env bash
MIRROR_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

PORT='8999'

(
  cd $MIRROR_DIR;
  python -m http.server $PORT > "$MIRROR_DIR/log/run-http-server.log" 2>&1 &
) &

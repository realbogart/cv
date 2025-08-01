#!/usr/bin/env bash

JSON_FILE=${1:-data.json}
OUTPUT_FILE=$(python3 -c "import json; print(json.load(open('$JSON_FILE'))['outputFilename'])" 2>/dev/null || echo "cv.pdf")

cp "$JSON_FILE" data.json
puppeteer print --margin-top 0 --margin-right 0 --margin-bottom 0 --margin-left 0 --wait-until networkidle0 index.html "$OUTPUT_FILE"


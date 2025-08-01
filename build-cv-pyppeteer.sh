#!/usr/bin/env bash

JSON_FILE=${1:-data.json}
OUTPUT_FILE=$(python3 -c "import json; print(json.load(open('$JSON_FILE'))['outputFilename'])" 2>/dev/null || echo "cv.pdf")

cp "$JSON_FILE" data.json
python convert.py 9876 "$OUTPUT_FILE" && xdg-open "$OUTPUT_FILE"

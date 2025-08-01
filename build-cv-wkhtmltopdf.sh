#!/usr/bin/env bash

JSON_FILE=${1:-data.json}
OUTPUT_FILE=$(python3 -c "import json; print(json.load(open('$JSON_FILE'))['outputFilename'])" 2>/dev/null || echo "cv.pdf")

cp "$JSON_FILE" data.json
wkhtmltopdf --enable-local-file-access -B 0 -L 0 -R 0 -T 0 index.html "$OUTPUT_FILE"

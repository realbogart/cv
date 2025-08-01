#!/usr/bin/env bash

# Default build script using Playwright
JSON_FILE=${1:-data.json}
./build-cv-playwright.sh "$JSON_FILE"
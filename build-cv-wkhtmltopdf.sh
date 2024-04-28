#!/usr/bin/env bash

wkhtmltopdf --enable-local-file-access -B 0 -L 0 -R 0 -T 0 index.html cv.pdf

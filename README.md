# CV Generator

A dynamic CV/resume website generator that creates PDFs from HTML/CSS using Playwright, with support for multiple JSON data files.

## Quick Start

### Default Build (Playwright)
```bash
./build-cv.sh [json_file]
```

Examples:
```bash
./build-cv.sh                # Uses data.json (default)
./build-cv.sh eva_mayer.json # Uses eva_mayer.json
```

### Alternative Build Methods

#### Using Nix
```bash
nix build                           # Local build
nix build github:realbogart/cv      # Build from GitHub
```

#### Other Methods
```bash
./build-cv-playwright.sh [json_file]  # Playwright with dynamic data
./build-cv-puppeteer.sh [json_file]   # Puppeteer (requires puppeteer-cli)
./build-cv-wkhtmltopdf.sh            # wkhtmltopdf
```

## Development

```bash
./develop-cv.sh                      # Start dev server and open browser
python server.py [port]              # Start HTTP server (default port 8000)
nix develop                          # Enter development shell
```

## Data Format

Create JSON files following the structure in `data.json`. The system supports dynamic loading of different resume data without rebuilding the HTML template.

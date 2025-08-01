# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a CV/resume website generator that creates a PDF from HTML/CSS using Playwright (default), Puppeteer, or wkhtmltopdf. The project uses Nix for reproducible builds and includes a simple Python development server.

## Build Commands

### Primary Build Method (Playwright - Default)
- `./build-cv.sh [json_file]` - Build PDF using Playwright (default, supports dynamic JSON data)
- `./build-cv-playwright.sh [json_file]` - Build PDF using Playwright with dynamic data loading

### Alternative Build Methods (Nix)
- `nix build` - Builds the CV PDF using Puppeteer via the Nix flake
- `nix build github:realbogart/cv` - Build from GitHub repository

### Other Build Methods
- `./build-cv-puppeteer.sh [json_file]` - Build PDF using Puppeteer (requires puppeteer-cli installed)
- `./build-cv-wkhtmltopdf.sh` - Build PDF using wkhtmltopdf (requires wkhtmltopdf installed)

### Development
- `./develop-cv.sh` - Start development server on port 9876 and open browser
- `python server.py [port]` - Start Python HTTP server with cache-busting headers (default port 8000)
- `nix develop` - Enter Nix development shell with all dependencies

## Architecture

### Core Files
- `index.html` - Main CV content with personal information, work experience, education, and skills
- `style.css` - CSS styling with custom fonts (Roboto, Source Serif Pro) and responsive layout
- `flake.nix` - Nix flake configuration defining build dependencies and process

### Assets
- `fonts/` - Contains Roboto and Source Serif Pro font files for consistent typography
- `icons/` - SVG icons for contact information (envelope, phone, GitHub, LinkedIn, etc.)

### Build Process
The build process converts the HTML/CSS into a PDF:
1. Uses Puppeteer CLI with specific margin settings (all margins set to 0)
2. Waits for `networkidle0` to ensure all resources are loaded
3. Outputs to `cv.pdf` in the build directory

### Development Server
The Python server (`server.py`) includes cache-busting headers to ensure changes are immediately visible during development.

## File Structure Notes
- No package.json - this is not a Node.js project despite using Puppeteer
- No test files - this is a static CV website
- Build outputs: `cv.pdf`, `output.pdf`, `result` (Nix build symlink)
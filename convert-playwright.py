import os
import sys
import shutil
import http.server
from threading import Thread
from playwright.sync_api import sync_playwright
from server import MyHTTPRequestHandler

if len(sys.argv) < 3:
    print("Usage: python convert-playwright.py <port> <output_file_path>")
    sys.exit(1)

port = int(sys.argv[1])
output_file_path = sys.argv[2]

def run_server(port):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

def run_browser(playwright, port, output_file_path):
    with playwright.chromium.launch(executable_path=shutil.which("chromium") or 'chromium') as browser:
        page = browser.new_page()
        page.goto(f'http://localhost:{port}')
        page.wait_for_function('document.fonts.ready');
        page.evaluate_handle('document.fonts.ready');
        page.pdf(path=output_file_path, format='A4', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        browser.close()
    print("PDF generation complete.")

def main():
    server_thread = Thread(target=run_server, args=(port,), daemon=True)
    server_thread.start()

    with sync_playwright() as playwright:
        run_browser(playwright, port, output_file_path)

if __name__ == "__main__":
    main()

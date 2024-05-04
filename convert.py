import asyncio
import os
import sys
from pyppeteer import launch
from threading import Thread
import http.server

from server import MyHTTPRequestHandler

if len(sys.argv) < 3:
    print("Usage: python convert.py <port> <output_file_path>")
    sys.exit(1)

port = int(sys.argv[1])
output_file_path = sys.argv[2]

def run_server(port):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, MyHTTPRequestHandler)
    httpd.serve_forever()

async def main():
    server_thread = Thread(target=run_server, args=(port,), daemon=True)
    server_thread.start()

    try:
        browser = await launch({
            'headless': True,
            'executablePath': 'chromium',
            'args': ['--no-sandbox', '--disable-web-security', '--disable-setuid-sandbox']
        })
        page = await browser.newPage()
        # Now navigating to the HTTP server running on localhost at the specified port
        await page.goto(f'http://localhost:{port}/index.html', {'waitUntil': 'networkidle0'})
        await page.pdf({
            'path': output_file_path,
            'format': 'A4',
            'printBackground': True,
            'margin': {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        })
        await browser.close()
    finally:
        # No need to kill the server, as it will exit when the main thread exits
        print("PDF generation complete.")

asyncio.get_event_loop().run_until_complete(main())

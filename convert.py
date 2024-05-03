import asyncio
import os
import sys
# import time
from pyppeteer import launch

if len(sys.argv) < 2:
    print("Usage: python convert.py <output_file_path>")
    sys.exit(1)

output_file_path = sys.argv[1]
current_script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(current_script_dir, 'index.html')

async def main():
    browser = await launch({ 'headless': True, 'executablePath': 'chromium', 'args': ['--no-sandbox', '--disable-web-security', '--disable-setuid-sandbox'] })
    page = await browser.newPage()
    await page.goto(f'file://{file_name}', {'waitUntil': 'load'})
    await page.waitForFunction('document.fonts.ready');
    # await page.evaluateHandle('document.fonts.ready');
    # time.sleep(1)
    await page.pdf({ 'path': output_file_path, 'format': 'A4', 'printBackground': True, 'margin': { 'top': 0, 'bottom': 0, 'left': 0, 'right': 0 } });
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

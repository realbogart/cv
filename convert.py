import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({ 'headless': True, 'executablePath': 'chromium' })
    page = await browser.newPage()
    await page.goto('file:///home/johan/projects/cv/index.html', {'waitUntil': 'networkidle0'})
    await page.pdf({ 'path': 'pyppeteer.pdf', 'format': 'A4' });
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

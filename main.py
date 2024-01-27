import asyncio
import pyppeteer
async def main():
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await page.goto('https://oxylabs.io/')
    await page.screenshot({'path': 'oxylabs_python.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
import asyncio

from pyppeteer import launch
from pyppeteer_stealth import stealth



async def stealth_test():
        browser = await launch(
            executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 
            headless=False,
            args=['--profile-directory=Default',
                  '--proxy-server=http://35.234.173.13:3128']
        )
        pages = await browser.pages()
        page = pages[-1]

        await stealth(
            page,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            locale="en-US,en;q=0.9",
            mask_linux=False,
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            disabled_evasions=[]
        )

        await page.setViewport({'width': 1920, 'height': 1080})
        await page.goto('https://www.whatismyip.com/')

asyncio.run(stealth_test())
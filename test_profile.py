import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def stealth_test():
    try:
        user_data_dir = 'C:\\Users\\Clement\\AppData\\Local\\Google\\Chrome\\User Data'
        profile_directory = 'Profile 9'

        print("Launching browser...")
        browser = await launch(
            executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            headless=False,
            userDataDir=user_data_dir,
            args=[
                f'--profile-directory={profile_directory}',
                '--proxy-server=http://35.234.173.13:3128'
            ]
        )

        print("Browser launched. Waiting for pages to load...")
        # Wait to ensure the browser has time to launch and load the profile

        pages = await browser.pages()
        if not pages:
            print("No pages found. Something went wrong.")
            return
        
        page = pages[-1]
        print(f"Opened page with URL: {page.url}")

        print("Applying stealth...")
        await stealth(page)

        await page.setViewport({'width': 1920, 'height': 1080})

        print("Navigating to the website...")
        await page.goto('https://bot.sannysoft.com/', {'waitUntil': 'networkidle2'})
        await asyncio.sleep(10)  # Wait for a few seconds to ensure the page loads

        print("Navigation complete.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Closing browser...")
        await browser.close()

# Run the script
asyncio.run(stealth_test())

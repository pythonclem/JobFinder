import asyncio
import csv
from pyppeteer import launch
from utilities import create_file, format_text, is_english


async def scrape_linkedin(job_titles):
    create_file()
    try:
        print("Launching browser...")
        browser = await launch(
            executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', 
            headless=False,
            userDataDir='C:\\Users\\Clement\\AppData\\Local\\Google\\Chrome\\User Data',
            args=['--profile-directory=Default']
        )
        pages = await browser.pages()
        page = pages[-1]
        await page.goto('https://www.linkedin.com/jobs/search/')
        await page.setViewport({'width': 1920, 'height': 1080})
        await asyncio.sleep(3)
        for job_title in job_titles:
            try:
                await page.waitForSelector('input[id^="jobs-search-box-keyword-id"]')
                await page.click('input[id^="jobs-search-box-keyword-id"]')
                await page.type('input[id^="jobs-search-box-keyword-id"]', job_title)
                await asyncio.sleep(2)
                await page.keyboard.press('Enter')
                await asyncio.sleep(3)
                # await page.click('button[id="searchFilter_timePostedRange"]')
                # await asyncio.sleep(1)
                # await page.click('input[id="timePostedRange-r86400"]')
                # await asyncio.sleep(1)
                # await page.click('button[aria-label^="Apply current filter to show"]')
                # await asyncio.sleep(3)
                for page_num in range(2, 4):
                    job_listings = await page.querySelectorAll('.jobs-search-results__list-item')
                    for job in job_listings:
                        await job.click({'button': 'left'})
                        await page.waitForSelector('.mt4')
                        description_element = await page.querySelector('div.mt4')
                        description = await page.evaluate('(element) => element.innerText', description_element)
                        if is_english(description):
                            formatted_description = format_text(description)
                            with open('jobs.csv', 'a', newline='', encoding='utf-8') as file:
                                writer = csv.writer(file)
                                writer.writerow([job_title, formatted_description])
                                print("Added a job to file")
                        await asyncio.sleep(5)
                    print("Scrolling...")
                    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                    await asyncio.sleep(3)
                    try:
                        await page.waitForSelector(f'button[aria-label="Page {page_num}"]')
                        await page.click(f'button[aria-label="Page {page_num}"]')
                    except:
                        pass
                    await asyncio.sleep(5)

            except Exception as e:
                print(f"An error occurred while typing the job title: {e}")

        await browser.close()
        print("Browser closed.")

    except Exception as e:
        print(f"An error occurred during browser launch or navigation: {e}")

if __name__ == '__main__':
    job_titles = ['software engineer']
    asyncio.run(scrape_linkedin(job_titles))
import asyncio
import csv
from pyppeteer import launch
import datetime
from langdetect import detect


def create_file():
    try:
        today = datetime.date.today()
        global filename
        filename = f'{today}-jobs.csv'
        with open(filename, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Description'])
    except FileExistsError:
        pass

def format_text(input_text):
    formatted_text = input_text.replace('"', "'")
    formatted_text = formatted_text.replace("\n", " ")
    formatted_text = formatted_text.strip()
    return formatted_text

def is_english(text):
    if detect(text) == 'en':
        return True
    else:
        return False




async def scrape_linkedin():
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
        job_titles = ['Junior Network']
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
                await page.click('button[id="searchFilter_timePostedRange"]')
                await asyncio.sleep(1)
                await page.click('input[id="timePostedRange-r86400"]')
                await asyncio.sleep(1)
                await page.click('button[aria-label^="Apply current filter to show"]')
                await asyncio.sleep(10)
                # job_listings = await page.querySelectorAll('.jobs-search-results__list-item')
                # first_five_jobs = job_listings[:2]
                # for job in first_five_jobs:
                #         await job.click({'button': 'left'})
                #         await page.waitForSelector('.mt4')
                #         description_element = await page.querySelector('div.mt4')
                #         description = await page.evaluate('(element) => element.innerText', description_element)
                #         if is_english(description):
                #             formatted_description = format_text(description)
                #             with open(filename, 'a', newline='', encoding='utf-8') as file:
                #                 writer = csv.writer(file)
                #                 writer.writerow([formatted_description])
                #         await asyncio.sleep(5)
                # await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
                # await asyncio.sleep(3)
                # if await page.waitForSelector('button[aria-label="Page 2"]'):
                #     await page.click('button[aria-label="Page 2"]')
                # await asyncio.sleep(5)

            except Exception as e:
                print(f"An error occurred while typing the job title: {e}")

        await browser.close()
        print("Browser closed.")

    except Exception as e:
        print(f"An error occurred during browser launch or navigation: {e}")

# Run the scrape_linkedin function
create_file()
asyncio.run(scrape_linkedin())
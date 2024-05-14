import asyncio
import csv
from pyppeteer import launch
from utilities import create_file, filename, format_text, is_english

async def scrape_indeed(job_titles):
    create_file()
    browser = None
    try:
        browser = await launch(executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', headless=False)
        page = await browser.newPage()
        result_pages = [0, 10, 20, 30]
        for job_title in job_titles:
            for result_page in result_pages:
                try:
                    url = f'https://nl.indeed.com/jobs?q={job_title}&l=Amsterdam&radius=50&lang=en&start={result_page}'
                    await page.goto(url)
                    await asyncio.sleep(5)
                    job_listings = await page.querySelectorAll('.resultContent')
                    if job_listings:
                        print(f"Found {len(job_listings)} jobs")
                    else:
                        print("Job listings empty")
                    for job in job_listings:
                        try:
                            button_selector = '[aria-label="sluiten"]'
                            button = await page.querySelector(button_selector)
                            if button:
                                await button.click()
                            await job.click({'button': 'left'})
                            await asyncio.sleep(3)
                            description_element = await page.querySelector('div#jobDescriptionText')
                            description = await page.evaluate('(element) => element.innerText', description_element)
                            formatted_description = format_text(description)
                            with open(filename, 'a', newline='', encoding='utf-8') as file:
                                writer = csv.writer(file)
                                writer.writerow([formatted_description])
                            await asyncio.sleep(3)
                            print(f"Added job to file")
                        except Exception as e:
                            print(f"Failed to process job: {str(e)}")
                            with open(filename, 'a', newline='', encoding='utf-8') as file:
                                writer = csv.writer(file)
                                writer.writerow([job_title, result_page])
                except Exception as e:
                    print(f"Failed to load page: {str(e)}")
                    with open(filename, 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow([job_title, result_page])
    finally:
        if browser:
            await browser.close()

if __name__ == '__main__':
    job_titles = ['network engineer']
    asyncio.run(scrape_indeed(job_titles))













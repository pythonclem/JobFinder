import asyncio
import csv
from pyppeteer import launch
import datetime

def create_file():
        try:
            today = datetime.date.today()
            global filename
            filename = f'{today}-jobs.csv'
            with open(filename, 'x', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Description'])
        except FileExistsError:
            pass 

async def scrape_indeed():
    try:
        browser = await launch(executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', headless=False)
        page = await browser.newPage()
        job_titles = ['System+Administrator']
        result_pages = [0, 10, 20, 30, 40]
        for job_title in job_titles:
            for result_page in result_pages:
                try:
                    url = f'https://nl.indeed.com/jobs?q={job_title}&l=Amsterdam&radius=50&lang=en&start={result_page}'
                    await page.goto(url)
                    await asyncio.sleep(3)
                    job_listings = await page.querySelectorAll('.resultContent')
                    first_two_jobs = job_listings[:2]
                    for job in first_two_jobs:
                        try:
                            button_selector = '[aria-label="sluiten"]'
                            button = await page.querySelector(button_selector)
                            if button:
                                await button.click()
                            await job.click({'button': 'middle'})
                            await asyncio.sleep(3)
                            pages = await browser.pages()
                            new_tab = pages[-1]
                            await new_tab.bringToFront()
                            await asyncio.sleep(3)
                            # Extract the job title
                            title_element = await new_tab.querySelector('[data-testid="jobsearch-JobInfoHeader-title"]')
                            title = await new_tab.evaluate('(element) => element.innerText', title_element)
                            # Extract the description
                            description_element = await new_tab.querySelector('div#jobDescriptionText')
                            description = await new_tab.evaluate('(element) => element.innerText', description_element)
                            with open('jobs.csv', 'a', newline='', encoding='utf-8') as file:
                                writer = csv.writer(file)
                                writer.writerow([title, description])
                            
                            await new_tab.close()
                            await asyncio.sleep(3)
                        except:
                            with open(filename, 'a', newline='', encoding='utf-8') as file:
                                writer = csv.writer(file)
                                writer.writerow([job_title, result_page])
                except:
                    with open(filename, 'a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow([job_title, result_page])
    finally:
        await browser.close()













        

if __name__ == '__main__':
    create_file()
    asyncio.run(scrape_indeed())

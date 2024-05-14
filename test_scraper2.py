import asyncio
from pyppeteer import launch


async def scrape_indeed():
    browser = await launch(executablePath='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', headless=False)
    page = await browser.newPage()


    await page.goto('https://www.indeed.com')
    await page.waitForSelector('#text-input-what')
    await page.waitForSelector('#text-input-where')
    await asyncio.sleep(2)
    await page.click('button[id="onetrust-accept-btn-handler"]')
    await asyncio.sleep(2)
    await page.type('#text-input-what', 'Software Engineer')
    await page.type('#text-input-where', 'Amsterdam')
    await page.click('button[type="submit"]')
    await asyncio.sleep(4)
    await page.click('button[id="filter-lang"]')
    job_listings = await page.querySelectorAll('.resultContent')
    for job in job_listings:
        await job.click({'button': 'middle'})
        await asyncio.sleep(4)
        pages = await browser.pages()
        new_tab = pages[-1]
        await new_tab.bringToFront()
        await asyncio.sleep(2)
        # Extract the job title
        title_element = await page.querySelector('[data-testid="jobsearch-JobInfoHeader-title"]')
        title = await page.evaluate('(element) => element.innerText', title_element)
        # Extract the description
        description_element = await new_tab.querySelector('div#jobDescriptionText')
        description = await new_tab.evaluate('(element) => element.innerText', description_element)
        print({'title': title, 'description': description})
        await new_tab.close()
        # # Extract the company name
        # company_element = await job.querySelector('div.company_location [data-testid="company-name"]')
        # company = await page.evaluate('(element) => element.textContent', company_element)


        # # Extract the location
        # location_element = await job.querySelector('div.company_location [data-testid="text-location"]')
        # location = await page.evaluate('(element) => element.textContent', location_element)

        # # Extract the description
        # description_element = await job.querySelector('div[id="jobDescriptionText"]')
        # description = await page.evaluate('(element) => element.textContent', description_element)


        # print({'title': title, 'company': company, 'location': location, 'description': description})















        

if __name__ == '__main__':
    asyncio.run(scrape_indeed())

import asyncio
from linkedinscraper import scrape_linkedin
from indeedscraper import scrape_indeed
from chatGPT import get_fit_score


async def find_me_a_job(job_titles):
    await scrape_indeed(job_titles)
    await scrape_linkedin(job_titles)
    await get_fit_score('jobs.csv')

if __name__ == '__main__':
    job_titles = ['technical support', 'soc analyst', 'junior cyber', 'information security']
    asyncio.run(find_me_a_job(job_titles))

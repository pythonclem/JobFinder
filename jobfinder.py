import asyncio
from linkedinscraper import scrape_linkedin
from indeedscraper import scrape_indeed
from chatGPT import get_fit_score

job_titles = []

async def find_me_a_job(job_titles):
    asyncio.run(scrape_indeed(job_titles))
    asyncio.run(scrape_linkedin(job_titles))
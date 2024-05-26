# Job Finder

**`Automating Job Searches to Find the Perfect Opportunity`**
   </br>

## 📜 The Why
Finding the perfect opportunity in an ocean of job posts is hard. You need an opportunity you’re passionate about, with the right experience requirement, the right technologies, not to mention the fact that many job posts require Dutch - en ik ben Nederlands aan het leren - but I’m not comfortable saying I know enough Dutch to work in Dutch. I was also told that knowing how to scrape is generally very useful, and it was a good opportunity to brush up my Python skills.

   </br>

## 📜 The What
Job Finder is a python scraping script for Linkedin and Indeed. It takes job titles as inputs, fetches the job posts, and builds a ChatGPT prompt to fish out the main requirements hiding somewhere in the job post. Experience requirements, technologies, and languages. It then outputs ChatGPT’s reply in an excel file, and it allows me to look at more job posts than I ever could if I did it manually.

   </br>

## 📜 The How
Job Finder leverages Pyppeteer, which is Puppeteer ported to Python. It can open a browser, run a search, and go post by post to extract the core and save it in an excel file. The scraping itself takes a few precautions like sleep times between clicks, and generally is designed to take a slow approach and not scrape robotically like mad. 

I’ve also integrated Pyppeteer-Stealth that allows me to manipulate the headers of the requests to try and, well, be stealthy about it. I’ve also set up a Google Cloud VM and installed Squid to make the requests go through a proxy, because I wanted some hands on experience configuring a proxy.

   </br>

## 📜 The Challenges
Learning Pyppeteer was an experience, as HTML and CSS aren’t really something I’ve focused on before. Scraping can be finicky, so getting it to work just right took a minute. Also, the integration with ChatGPT’s API wasn’t the easiest, as I wasn’t getting the responses I was hoping for. Luckily, after a quick prompt engineering learning session, I started to get exactly what I was looking for.

   </br>

## 📜 The Lessons
This project came to me as I was lamenting the inefficiencies of the job hunt and realized I have the power to do something about it. I had that very thought many times since. Pick up some skills, and go for it. The part about the prompt engineering was very beneficial as well. If AI is a tool, knowing how to get the most out of it is a strength. I’m by no means an expert - but I’m significantly better at using it than I was before.

   </br>

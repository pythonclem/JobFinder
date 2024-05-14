from dotenv import load_dotenv
import os
from openai import OpenAI

def get_fit_score(job_post):
  load_dotenv()
  api_key = os.getenv('OPENAI_API_KEY')
  client = OpenAI(api_key=api_key)
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Return a fit score, and a 1 sentence explanation. Disqualify jobs that require Dutch (score 0). Look for low experience requirements. Do not penalize for lack of degree."},
    {"role": "user", "content": f"{job_post}"},
  ]
)

  print(completion.choices[0].message)



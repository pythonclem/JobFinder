from dotenv import load_dotenv
import os
from openai import OpenAI
import csv

def get_fit_score(filename):
  load_dotenv()
  api_key = os.getenv('OPENAI_API_KEY')
  client = OpenAI(api_key=api_key)
  with open(filename, 'r', newline='', encoding='utf-8') as inputfile:
      reader = csv.reader(inputfile)
      rows = list(reader)

  with open('jobs_ranked.csv', 'a', newline='', encoding='utf-8') as outputfile:
      writer = csv.writer(outputfile)
          
      for row in rows:  
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "Start your answer with 'Fit Score: ' (1 to 10, 10 highest) and mention the #1 reason for the score. Disqualify jobs that require Dutch (score 0). Disqualify jobs that require 3+ years of experience (score 0). Do not penalize for lack of degree."},
          {"role": "user", "content": f"Candidate holds a bachelor degree, Network+ and Security+ certifications, and has knowledge of Linux, Python, and IT - but no work experience. Role: {row[1]}"},
        ]
      )

        answer = completion.choices[0].message
        row.append(answer)
        writer.writerow(row)
        print("Job ranked")
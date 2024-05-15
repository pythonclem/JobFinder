from dotenv import load_dotenv
import os
from openai import OpenAI
import csv
import json
import time

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
          {"role": "system", "content": "You will get a job posting delimited by triple quotes, and 4 questions to answer on said job post. Make sure to read the job post before answering each question. Return a JSON with a dictionary with the keys 1, 2, 3, 4. Keep your answers brief."},
          {"role": "user", "content": f"Candidate holds a bachelor degree, Network+ and Security+ certifications, and has knowledge of Linux, Python, and IT - but no work experience. Role: {row[1]}"},
        ]
      )

        answer = completion.choices[0].message
        row.append(answer)
        writer.writerow(row)
        print("Job ranked")


def jobpost_analyzer(filename):

  start_time = time.time()
  load_dotenv()
  api_key = os.getenv('OPENAI_API_KEY')
  client = OpenAI(api_key=api_key)

  with open(filename, 'r', newline='', encoding='utf-8') as inputfile:
      reader = csv.reader(inputfile)
      rows = list(reader)

  with open('jobs_ranked3.csv', 'a', newline='', encoding='utf-8') as outputfile:
      writer = csv.writer(outputfile)

      for row in rows:  
        q0 = "Question 0: What is the name of the company?"
        q1 = "Question 1: What is the title of the position?"
        q2 = "Question 2: Does the job posting require the Dutch language? Yes/No"
        q3 = "Question 3: How many years of experience is requested? Integer (best option) / A lot / A little / Not mentioned"
        q4 = "Question 4: What technologies and tools are mentioned?"
        q5 = "Question 5: Rate this position from 1 to 10 for relevance to networks and cybersecurity."
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
              {"role": "system", "content": "You will get a job posting delimited by xml tags, and 6 questions to answer on said job post. Make sure to read the job post before answering each question. Return a JSON with a dictionary with the keys 0, 1, 2, 3, 4, 5. Keep your answers brief and in simple strings."},
              {"role": "user", "content": f"<tag> {row} </tag> {q0} {q1} {q2} {q3} {q4} {q5}"},
            ]
          )
        try:
          answer = completion.choices[0].message.content
          parsed_response = json.loads(answer)
          analyzed_row = []
        
          for x in range (0, 6):
            shortanswer = parsed_response[f"{x}"]
            analyzed_row.append(shortanswer)
            
          writer.writerow(analyzed_row)
          print("Job analyzed")
        except:
           print("Error Parsing")

  end_time = time.time()
  elapsed_time = end_time - start_time
  print(f"Function executed in {elapsed_time:.2f} seconds")
  print(f"Average time to analyze a job: {elapsed_time / len(rows)}")

jobpost_analyzer("jobs.csv")
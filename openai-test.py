from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)


requirments = ""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Return a JSON with a fit score, and a 1 sentence explanation. Disqualify jobs that require Dutch (score 0). Look for low experience requirements. Do not penalize for lack of degree."},
    {"role": "user", "content": "The candidate: Bachelor's degree. Network+ and security+ certifications, strong knowledge of IT, Python, Linux. Looking for a first job in IT or cyber. Role requirements: Respond to and resolve in person Frist line IT incidents logged via our global IT Service Desk, providing solutions to known incidents and problems for our internal customer base, diagnosing and working to resolve undefined problems as they occur Effective incident queue management with ownership of logged incidents via current call logging toolsets (Remedy/Service Now). Prioritise ticket resolution workload on predefined Service Level Agreements Awareness and correct use of key escalation points for both PC hardware and software incidents and service provision Perform PC upgrades where required using defined internal processes, including data backups and restore Perform imaging of workstations (both laptops and desktops) where required Ensure good knowledge of all PC hardware models in the environment, including specifications and internal customer PC model eligibility criteria IT support for events such as new joiner inductions and VIP meetings when required Input where required to the successful delivery of team important metrics Support internal tailored support environments where requested Working effectively with required external suppliers who are used to deliver components of our service, such as data recovery and IT consumable provision Regularly review processes utilised within the team, propose and implement improvements with necessary approvals to ensure processes remain relevant for the Local Support team Requirements Provide technical support for resolution of customer IT problems,incidents, issues, requests and queries Liaise with other support teams, or product teams as required to resolve requests/issues in a timely manner Ensure proper documentation, notification, escalation,tracking and follow up of all incidents Primary responsibilities are focused on customer contact, not transaction processing Dutch language proficiency is Must"},
  ]
)

print(completion.choices[0].message)



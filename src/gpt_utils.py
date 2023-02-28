import os
import openai
from dotenv import load_dotenv
import datetime
import json
from typing import List

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def makeGptCall(message: str) -> str:
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=message,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  return response.choices[0].text

def createPrompt(planText: str) -> str:
  nowTimestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
  return f"""
    It is now {nowTimestamp}. Create an array of JSON objects
    for Google Calendar API events in the same timezone
    to capture the events in this statement: {planText}.
  """

class CalendarEvent:
  def __init__(self, summary, startTime, endTime):
    self.summary = summary
    self.startTime = startTime
    self.endTime = endTime

def convertTextToEvents(text: str):
  eventJson = makeGptCall(text)
  try:
    json.loads(eventJson)
  except ValueError:
    prompt = "Reformat this as valid JSON:\n {eventJson}"
    eventJson = makeGptCall(prompt)

  events = [CalendarEvent(**e) for e in json.loads(eventJson)]
  return events
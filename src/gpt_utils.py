import os
import openai
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

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
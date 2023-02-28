from src.gpt_utils import createPrompt, convertTextToEvents, CalendarEvent
from mock import patch
import json

EVENT = {
    "summary": "Gym at 11am",
    "start": None,
    "end": None,
}

def test_createPrompt():
    planText = "Gym at 11am"
    prompt = createPrompt(planText)
    assert planText in prompt

@patch('src.gpt_utils.makeGptCall')
def test_convertTextToEvents(mock_makeGptCall):
    mock_makeGptCall.return_value = json.dumps([EVENT])
    planText = "Gym at 11am"
    prompt = createPrompt(planText)
    events = convertTextToEvents(prompt)
    assert len(events) == 1

@patch('src.gpt_utils.makeGptCall')
def test_convertTextToEvents_retrying(mock_makeGptCall):
    validResponse = json.dumps([EVENT])
    mock_makeGptCall.side_effect = ["some invalid json response", validResponse]

    planText = "Gym at 11am"
    prompt = createPrompt(planText)
    events = convertTextToEvents(prompt)
    assert len(events) == 1
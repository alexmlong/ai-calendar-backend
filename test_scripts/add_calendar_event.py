from src.gcal_utils import addEventToCalendar
from src.gpt_utils import CalendarEvent

event = CalendarEvent("Gym at 2pm", None, None)
addEventToCalendar(event)
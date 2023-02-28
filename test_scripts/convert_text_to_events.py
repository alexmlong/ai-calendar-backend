from src.gpt_utils import convertTextToEvents

planText = "Gym at 11am"
events = convertTextToEvents(planText)
print(events)
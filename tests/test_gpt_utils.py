from src.gpt_utils import createPrompt

def test_createPrompt():
    planText = "Gym at 11am"
    prompt = createPrompt(planText)
    assert planText in prompt
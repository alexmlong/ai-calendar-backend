from flask import Flask, request, session, redirect
from google.oauth2.credentials import Credentials
from gcal_utils import addEventToCalendar, CLIENT_CONFIG, SCOPES, REDIRECT_URL, generateAuthUrl, generateFlow
from gpt_utils import convertTextToEvents
from google_auth_oauthlib.flow import Flow

app = Flask(__name__)

@app.route("/")
def hello_world():
    if 'credentials' not in session:
        authUrl = generateAuthUrl()
        return f"<p>You're not authenticated yet! Click <a href='{authUrl}'>here to give the app access</a></p>"
    else:
        return "<p>Hello, authenticated user!<p>"

@app.route('/oauth2callback')
def auth_callback():
    flow = generateFlow()

    flow.fetch_token(authorization_response=request.url)

    session['credentials'] = Credentials.to_authorized_user_info(flow.credentials)

    return redirect('/')

@app.route('/submit_plan_text', methods=["POST"])
def handle_plan_text():
    planText = request.json['planText']
    events = convertTextToEvents(planText)
    for event in events:
      addEventToCalendar(event)

if __name__ == '__main__':
    app.run(port=3000)
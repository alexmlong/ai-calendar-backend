import os
from dotenv import load_dotenv
from google import oauth2
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from gpt_utils import CalendarEvent
from google_auth_oauthlib.flow import Flow

load_dotenv()

CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
REDIRECT_URL = os.environ.get('GOOGLE_REDIRECT_URL')

CLIENT_CONFIG = {
    'web': {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'userinfo_uri': 'https://www.googleapis.com/oauth2/v1/userinfo',
    },
}

SCOPES=['https://www.googleapis.com/auth/calendar']

def generateFlow():
    return Flow.from_client_config(
        client_config=CLIENT_CONFIG,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URL,
    )

def generateAuthUrl():
    flow = generateFlow()                                       

    auth_url, _ = flow.authorization_url(
        access_type='offline',
        prompt='consent',
        login_hint='primary'
    )

    return auth_url
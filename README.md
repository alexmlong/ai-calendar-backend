# AI Calendar Backend
Backend for AI Calendar prototype made in a hackathon with my girlfriend :)

This provides a service which is expected to be called to from a front end app, allowing the user to convert natural language into Google calendar event JSON objects via OpenAI's GPT-3 API.

## Environment variables

- OPENAI_API_KEY: The API key to use when connecting to GPT-3
- GOOGLE_CLIENT_ID: Client ID for Google app, e.g. 12345-abcdef.apps.googleusercontent.com
- GOOGLE_CLIENT_SECRET: Client secret for Google app, e.g. ABC--1234_
- GOOGLE_REDIRECT_URL: The URL for Google to redirect the user to after providing account access, e.g. http://localhost:3000/oauth2callback

## How this works

This service has two main functions:

### 1. To proxy requests from a client app to GPT-3

This function is fulfilled through a server endpoint. The requests to the endpoint are expected to be natural language explanations of how a user is planning their day.

This service prefaces the text describing the daily plan with instructions to GPT-3, specifically to convert them into Google calendar event JSON objects.

It then sends the request to GPT-3 and receives the JSON objects. It validates that they can be parsed, and if not, makes a retry attempt to GPT-3.

Once it has valid event objects, the service performs its second function:

### 2. To interact with the Google Calendar API in order to create events

A precursor to this functionality is obtaining permission from a user to interact with their Google calendar.

Once it has done that, it creates events in their calendar as per the instructions in the previous section.

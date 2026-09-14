import datetime
import os
from typing import List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly",
          "https://www.googleapis.com/auth/calendar"]

"""
Fetch credentials to access users Calender
"""
def fetch_creds():

    #Receive a user ID from the frontend and store creds so we can fetch everytime we need to
    
    creds = None
    
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not os or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds
    
def create_calender_event(tool_input: dict):

    event = {

    }
    service.events().insert(calenderId="primary", body=event).execute()
    return "Event added to Calender"
    

def list_calender_events(tool_input: dict) -> str:

    creds = fetch_creds()
    if not creds:
        return "Failure"

    start = tool_input["start"]
    end = tool_input["end"]
    location_type = tool_input["location_type"]
    maxResults = tool_input["maxResults"]

    try:
        service = build("calender", "v3", credentials=creds)
        
        #Call CalenderAPI
        now = datetime.datetime.now(tz=datetime.date.utc).isoformat()
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=maxResults,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )

        events = events_result.get("items", [])
        if not events:
            return "No upcoming events found."

        start_and_event_name = ""
        for event in events:
            start = event["start"].get("datetime", event["start"].get("date"))
            start_and_event_name += start + " " + event["summary"] + "/n"
        return start_and_event_name
        
    except HttpError as error:
        return str(error)

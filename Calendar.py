from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from tkinter import *
import tkinter

from DateAndTime import DateAndTime

# CODE IN MAIN FUNCTION TAKEN AND MODIFIED FROM https://developers.google.com/calendar/api/quickstart/python
class Calendar:
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    COUNTER = -1

    def __init__(self, master, root):
        self.master = master
        self.createLabel(root)
        self.createUI()


    def main():
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', Calendar.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', Calendar.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)

            # Call the Calendar API
            current_day = datetime.datetime.utcnow().isoformat() + 'Z'
            end_of_day = Calendar.get_end_of_day()
            events_result = service.events().list(calendarId='primary', timeMin=current_day, timeMax=end_of_day, singleEvents=True, orderBy='startTime').execute()
            events = events_result.get('items', [])

            ret_val = []
            if not events:
                print('No upcoming events found.')
                return ret_val

            # Prints the start and name of the events
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                end = event['end'].get('dateTime', event['end'].get('date'))
                print([start, end, event['summary']])
                ret_val.append([start, end, event['summary']])

            return ret_val

        except HttpError as error:
            print('An error occurred: %s' % error)


    # Returns the local midnight time in UTC time 
    def get_end_of_day():
        current_time = datetime.datetime.now()
        tomorrow = current_time + datetime.timedelta(days=1)
        # Calculates how many seconds are until midnight
        seconds_until_midnight = (datetime.datetime.combine(tomorrow, datetime.time.min) - current_time).seconds
        return ((datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds_until_midnight)).isoformat() + 'Z')


    def time_converter(date_time_string):
        start_dt = date_time_string.split('T')
        start_time = start_dt[1].split('-')[0]
        d = datetime.datetime.strptime(start_time, "%H:%M:%S")
        return d.strftime("%-I:%M %p")


    # Formats the event data
    def formatted_data():
        ret_val = "Your Schedule\n"
        events_data = Calendar.main()
        
        if len(events_data) == 0:
            return ""
        
        for event in events_data:
            start_time = str(Calendar.time_converter(event[0]))
            end_time = str(Calendar.time_converter(event[1]))
            event_name = event[2]
            ret_val += start_time + " - " + end_time + " " + event_name + "\n"

        print(ret_val)
        return ret_val


    def createLabel(self, root):
        global calendarLabel
        calendarLabel = tkinter.Label(root, bg="black", fg="white", font=("Arial", 20))
        calendarLabel.place(relx=0.0, rely=0.15, anchor=NW)
        calendarLabel.after(0, self.createUI)


    def createUI(self):
        currentMinutesAndSeconds = DateAndTime.getMinutesAndSeconds()
        if (currentMinutesAndSeconds == "00:00" and Calendar.COUNTER == 0) or Calendar.COUNTER == -1:
            calendarLabel.configure(text=str(Calendar.formatted_data()))
            Calendar.COUNTER = 1
        if currentMinutesAndSeconds != "00:00" and Calendar.COUNTER == 1:
            Calendar.COUNTER = 0
        calendarLabel.after(1000, self.createUI)





# PERSONAL NOTES ON HOW I WILL USE THIS
# Every hour update calendar list and keep end date midnight somehow -> will have to transition to next day though when we get to midnight
# Currently I could reuse the code as it more or less does what I want
# Maybe look for a better way to get all the "events" for the day
# Do I push credentials.json to Github? 
# Calendar looks possible! 
# Need to cite where I got the code from -> https://developers.google.com/calendar/api/quickstart/python


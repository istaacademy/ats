from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os.path


def set_meeting(start: str, end: str, gmails: dict = None):
    # If modifying these SCOPES, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/calendar']

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Assuming you have the creds from the authorization step
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': " جلسه مصاحبه با hr (کارخانه هیولاسازی Front-end)",
        'description': "مصاحبه",
        'start': {
            'dateTime': start if start else '2024-02-29T14:00:00-07:00',
            'timeZone': 'Asia/Tehran',
        },
        'end': {
            'dateTime': end if end else '2024-02-29T16:00:00-07:00',
            'timeZone': 'Asia/Tehran',
        },
        'attendees': [
            {'email': 'smk182018@gmail.com'},
            {'email': 'kashaniBayley@gmail.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
        'conferenceData': {
            'createRequest': {
                'requestId': 'some-unique-string'
            }
        },
    }

    # Insert the event into the calendar
    event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
    print(event.get('hangoutLink'))
    print('Event created: %s' % (event.get('htmlLink')))
    return event.get('hangoutLink')

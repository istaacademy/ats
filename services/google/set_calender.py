from datetime import datetime
from auth import authentication


def set_meeting(start: datetime, end: datetime, volunteer_email: str, interviewer_email: str, date):
    event = {
        'summary': " جلسه مصاحبه با hr (کارخانه هیولاسازی Front-end)",
        'description': "مصاحبه",
        'start': {
            'dateTime': f"{date}T{start}" if start else '2024-02-29T14:00:00-07:00',
            'timeZone': 'Asia/Tehran',
        },
        'end': {
            'dateTime': f"{date}T{end}" if end else '2024-02-29T16:00:00-07:00',
            'timeZone': 'Asia/Tehran',
        },
        'attendees': [
            {'email': volunteer_email},
            {'email': interviewer_email},
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
    service = authentication(service_name="calender")
    event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
    print(event.get('hangoutLink'))
    print('Event created: %s' % (event.get('htmlLink')))
    return event.get('hangoutLink')

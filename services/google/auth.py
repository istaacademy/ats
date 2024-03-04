from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os.path


def authentication(service_name: str = "calender"):
    # If modifying these SCOPES, delete the file token.json.
    SCOPES_C = ['https://www.googleapis.com/auth/calendar']
    SCOPES_G = ['https://www.googleapis.com/auth/gmail.send']

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    cwd = os.getcwd()
    token_calender_path = f'{cwd}/token_calender.json'
    token_gmail_path = f'{cwd}/token_gmail.json'
    if os.path.exists(token_calender_path if service_name == "calender" else token_gmail_path):
        creds = Credentials.from_authorized_user_file(token_calender_path if service_name == "calender"
                                                      else token_gmail_path,
                                                      SCOPES_C if service_name == "calender" else SCOPES_G)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                f'{cwd}/credentials.json',
                SCOPES_C if service_name == "calender" else SCOPES_G)

            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_calender_path  if service_name == "calender" else token_gmail_path, 'w') as token:
            token.write(creds.to_json())

    # Assuming you have the creds from the authorization step
    if service_name == "calender":
        service = build('calendar', 'v3', credentials=creds)
    else:
        service = build('gmail', 'v1', credentials=creds)
    return service
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from auth import authentication
from email import encoders
import os.path
import base64

cwd = os.getcwd()
file_path = f'{cwd}/test.pdf'


def create_message(sender, to, subject, body):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # Create a MIMEText object with HTML content
    msg = MIMEText(body, 'html')
    message.attach(msg)

    # Attach the file
    attachment = MIMEBase('application', 'octet-stream')
    with open(file_path, 'rb') as file:
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
    message.attach(attachment)

    raw_message = base64.urlsafe_b64encode(message.as_bytes())
    raw_message = raw_message.decode('utf-8')
    return {'raw': raw_message}

    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print(f'An error occurred: {error}')


# Authenticate to the Gmail API
service = authentication(service_name="gmail")

message = ("اسماعیل جان"
           "")

# Send an email
name = "اسماعیل"
email_body_html = (f'<p>سلام  {name},</p><p>This is a personalized test email sent from Python via Gmail API with HTML '
                   f'content.</p>')

test_message = create_message('istaacademyinfo@gmail.com',
                              'smk182018@gmail.com', 'Task',
                              email_body_html)
send_message(service, 'me', test_message)

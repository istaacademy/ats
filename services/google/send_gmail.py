from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from services.google.auth import authentication
from email import encoders
from services.google.generate_message import generate_message
import os.path
import base64

cwd = os.getcwd()
file_path = f'{cwd}/services/google/test.pdf'


def _create_message(sender, to, subject, body, status: str = None):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # Create a MIMEText object with HTML content
    msg = MIMEText(body, 'html')
    message.attach(msg)

    if status == "task":
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


def _send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        print('Message Id: %s' % message['id'])
        return True
    except Exception as error:
        print(f'An error occurred: {error}')


def send_email(name: str, status: str, receiver_email: str):
    # Authenticate to the Gmail API
    service = authentication(service_name="gmail")
    # HTML template with variables
    email_body_html = generate_message(name, status)
    test_message = None
    if status == "task":
        test_message = _create_message('istaacademyinfo@gmail.com',
                                       receiver_email, 'مرحله اول: چالش فنی',
                                       email_body_html, status="task")
    elif status == "accept-task":
        test_message = _create_message('istaacademyinfo@gmail.com',
                                       receiver_email, 'مرحله دوم: مصاحبه با منابع انسانی',
                                       email_body_html)
    elif status == "accept-hr":
        test_message = _create_message('istaacademyinfo@gmail.com',
                                       receiver_email, 'مرحله پایانی - پرداخت شهریه',
                                       email_body_html)
    elif status == "reject-hr" or status == "reject-task":
        test_message = _create_message('istaacademyinfo@gmail.com',
                                       receiver_email, 'Reject',
                                       email_body_html)

    return _send_message(service, 'me', test_message)

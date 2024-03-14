from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from services.google.auth import authentication
from email import encoders
import os.path
import base64

cwd = os.getcwd()
file_path = f'{cwd}/services/google/test.pdf'


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
        return True
    except Exception as error:
        print(f'An error occurred: {error}')


def send_email(name: str, family: str, receiver_email: str):
    # Authenticate to the Gmail API
    service = authentication(service_name="gmail")
    # HTML template with variables

    recipient_name = f" {family}{name} "

    email_body_html = f"""
    <!DOCTYPE html>
    <html>
       <head>
          <style>
             body {{
             font-family: Sans-serif;
             font-size: 20px;
             text-align: right;
             direction: rtl;
             }}
             .id{{
             text-align: left;
             direction: ltr;
             }}
          </style>
       </head>
       <body>
          <h4>{recipient_name}</h4>
          <p>سلام</p>
          <p>  امیدوارم خوب باشی</p>
          <p>         به پیوست این ایمیل تسک مرحله اول مصاحبه رو براتون فرستادیم.</p>
            <p>
             راه‌های ارتباطی توی تسک عنوان شدن. اگر سوالی داشتید یا نکته و ابهامی وجود داشت، می‌تونید از طریق همین راه‌ها با ما در ارتباط باشید. برای انجام این تسک ۴۸ ساعت از زمان دریافت این ایمیل فرصت دارید.
          </p>
          <div class="id">
             @ista_support
          </div>
       </body>
    </html>
    """
    test_message = create_message('istaacademyinfo@gmail.com',
                                  receiver_email, 'Task',
                                  email_body_html)

    return send_message(service, 'me', test_message)

from celery import shared_task
from services.google.send_gmail import send_email
import time


@shared_task(queue='email', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def send_email_task(name, family, receiver_email):
    return send_email(name, family, receiver_email)


@shared_task(queue='git', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def tp1():
    return


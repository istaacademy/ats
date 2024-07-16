from celery import shared_task
from services.google.send_gmail import send_email
from volunteer.models import Task
import time


@shared_task(queue='email', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def send_email_task(name, receiver_email, volunteer_id):
    send_email(name, "task", receiver_email)
    Task.objects.create(volunteer_id=volunteer_id)


@shared_task(queue='email', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def send_email_accept_task(name, receiver_email):
    send_email(name, "accept-task", receiver_email)


@shared_task(queue='email', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def send_email_accept_hr(name, receiver_email):
    send_email(name, "accept-hr", receiver_email)


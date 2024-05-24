from celery import shared_task
from services.google.set_calender import set_meeting
from calender.models import Event


@shared_task(queue='email', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def create_meeting(start, end, volunteer_email, interviewer_email, date, event_id):
    link_meeting = set_meeting(start, end, volunteer_email, interviewer_email, date)
    obj = Event.objects.get(id=event_id)
    obj.link_meeting = link_meeting
    obj.save()


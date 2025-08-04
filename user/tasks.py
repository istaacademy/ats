from celery import shared_task
from services.sms.client import SMS


@shared_task(queue='sms', default_retry_delay=5, retry_kwargs={'max_retries': 5})
def send_sms(verification_code, phone):
    sms_service = SMS("faraz", phone=phone, message=verification_code)
    data = sms_service.send_message()
    if data.json()["meta"]["status"]:
        return "send message successfully"



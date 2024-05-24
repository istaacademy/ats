from datetime import timedelta
from celery import Celery
from kombu import Exchange, Queue
import os
import logging

logging.basicConfig(filename='../app.log', level=logging.ERROR, format='%(levelname)s %(message)s')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kernel.settings.development')


app = Celery('kernel')
app.config_from_object("kernel.settings.base", namespace="CELERY")
app.autodiscover_tasks()

app.conf.task_queues = [
    Queue('email', Exchange('email'), routing_key='email'),
    Queue('git', Exchange('git'), routing_key='git'),
    Queue('meeting', Exchange('meeting'), routing_key='meeting'),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1
app.conf.result_expires = timedelta(days=1)

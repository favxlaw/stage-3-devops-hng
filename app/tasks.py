from . import celery
from .utils import send_email, log_time

@celery.task
def send_email_task(email):
    send_email(email)

@celery.task
def log_time_task():
    log_time()

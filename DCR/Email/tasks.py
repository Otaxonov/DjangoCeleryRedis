from django.core.mail import send_mail
from celery import shared_task

@shared_task
def SendMailTask(receiver, message):
    send_mail(subject='DCR Mail App', message=message, from_email='celery@gmail.com',recipient_list=[receiver], fail_silently=True)

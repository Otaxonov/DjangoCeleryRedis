from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def SendMailTask(receiver, message):
    send_mail(subject='DCR Mail App', message=message, from_email='Celery@gmail.com',recipient_list=[receiver], fail_silently=True)

@shared_task
def GoodMorning():
    users = User.objects.all()

    for user in users:
        if user.email:
            send_mail(subject='DCR Mail App', message='Good Morning', from_email='Celery@gmail.com', recipient_list=[user.email], fail_silently=True)
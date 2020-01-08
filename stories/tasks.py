from celery import shared_task
from .models import Subscriber
from django.core.mail import send_mail
from django.conf import settings

# @shared_task
# def sum(a, b):
#     return a+b

@shared_task
def send_mail_to_subscribers():
    subscribers = list(Subscriber.objects.values_list('email', flat=True))
    send_mail(subject='Our daily news on webpage', message='',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=subscribers)
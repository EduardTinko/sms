from celery import shared_task
from twilio.rest import Client
from django.conf import settings


client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@shared_task
def send_sms(receiver, message):
    print("2")
    print(settings.TWILIO_ACCOUNT_SID)
    message = client.messages.create(body=message, from_="+17152452157", to=receiver)
    print("send")
    return message.sid

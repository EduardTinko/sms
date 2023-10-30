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


# docker run -d -p 5672:5672 rabbitmq
# setx TWILIO_ACCOUNT_SID 'ACf5f68475b5b665b31654e0efa6f850a1'
# setx TWILIO_AUTH_TOKEN "103097735d572fbd47bc50d494f7cc01"
# celery -A site_sms worker -l INFO

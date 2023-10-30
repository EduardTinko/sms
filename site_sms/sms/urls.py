from django.urls import path

from .views import receiver_message_form

urlpatterns = [path("send_sms", receiver_message_form, name="receiver_message_form")]

from django.shortcuts import render

from .forms import SendSmsForm
from .tasks import send_sms

# Create your views here.


def receiver_message_form(request):
    if request.method == "GET":
        form = SendSmsForm()
        return render(request, "send_sms_form.html", {"form": form})
    form = SendSmsForm(request.POST)
    if form.is_valid() and request.method == "POST":
        send_sms.delay(form.cleaned_data["receiver"], form.cleaned_data["message"])
    return render(request, "send_sms_form.html", {"form": form})

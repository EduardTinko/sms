from django.shortcuts import render

from .forms import SendSmsForm
from .tasks import send_sms

# Create your views here.


def receiver_message_form(request):
    print("1")
    if request.method == "GET":
        print("2")
        form = SendSmsForm()
        return render(request, "send_sms_form.html", {"form": form})
    form = SendSmsForm(request.POST)
    print("3")
    if form.is_valid() and request.method == "POST":
        print("4")
        send_sms.delay(form.cleaned_data["receiver"], form.cleaned_data["message"])
        print("5")
    return render(request, "send_sms_form.html", {"form": form})

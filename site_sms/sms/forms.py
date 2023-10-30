from django import forms


class SendSmsForm(forms.Form):
    receiver = forms.CharField(max_length=20)
    message = forms.CharField(max_length=100)

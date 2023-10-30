import phonenumbers
from django import forms


class SendSmsForm(forms.Form):
    receiver = forms.CharField(max_length=20)
    message = forms.CharField(max_length=100)

    def clean_receiver(self):
        receiver = self.cleaned_data["receiver"]
        try:
            parsed = phonenumbers.parse(receiver, None)
            if not phonenumbers.is_valid_number(parsed):
                raise forms.ValidationError("The phone number is not valid")
        except phonenumbers.NumberParseException as e:
            raise forms.ValidationError("The phone number is incorrect")
        return phonenumbers.format_number(
            parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

import re

from django import forms

class SendMailForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(empty_value="123@gmail.com")
    phone = forms.CharField(max_length=10, required=False)
    adress = forms.CharField(max_length=60, required=False)
    zip_code = forms.CharField(max_length=5, required=False, empty_value="75000")
    object = forms.CharField(max_length=255)
    message = forms.CharField(empty_value="Votre message ici")




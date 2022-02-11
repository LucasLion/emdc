import re

from django import forms

class SendMailForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    email = forms.EmailField(empty_value="123@gmail.com", widget=forms.EmailInput
                           (attrs={'placeholder': 'E-mail'}))
    phone = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={'placeholder': 'Téléphone'}))
    adress = forms.CharField(max_length=60, required=False, widget=forms.TextInput(attrs={'placeholder': 'Adresse'}))
    object = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Objet'}))
    message = forms.CharField(empty_value="Votre message ici",  widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': '5'}))




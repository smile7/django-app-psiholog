# from django import forms
from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

""" 
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=20)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget = forms.Textarea, max_length=20000)
 """
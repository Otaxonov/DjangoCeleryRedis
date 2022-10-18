from django import forms

class SendMailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    message = forms.CharField(widget=forms.Textarea())
from django import forms

from emails_messages.models import EmailMessage


class EmailMessageForm(forms.ModelForm):
    class Meta:
        model = EmailMessage
        fields = ['title', 'description']

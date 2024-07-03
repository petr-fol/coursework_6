from django import forms

from messages.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'description']

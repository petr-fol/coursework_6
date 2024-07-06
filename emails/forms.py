from django import forms

from emails.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['clients', 'message', 'title', 'start_date', 'periodicity']
        
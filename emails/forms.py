from django import forms

from emails.models import Email


class EmailsForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'

from django import forms

from clients.models import Client  # Subject
from config.style import StyleFormMixin


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        # исключение полей ниже
        exclude = ['slug']



# class SubjectForm(StyleFormMixin, forms.ModelForm):
#     class Meta:
#         model = Subject
#         fields = ['title', 'description',]  # 'student'

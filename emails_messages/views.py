from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from emails_messages.forms import EmailMessageForm
from emails_messages.models import EmailMessage


# Create your views here.
class EmailMessageCreateView(CreateView):
    model = EmailMessage
    form_class = EmailMessageForm
    context_object_name = 'email_message_create'
    success_url = reverse_lazy('email_message_list')


class EmailMessageListView(ListView):
    model = EmailMessage
    context_object_name = 'emails_messages'


class EmailMessageDetailView(DetailView):
    model = EmailMessage
    context_object_name = 'email_message'


class EmailMessageUpdateView(UpdateView):
    model = EmailMessage
    form_class = EmailMessageForm
    success_url = reverse_lazy('email_message_detail')


class EmailMessageDeleteView(DeleteView):
    model = EmailMessage
    form_class = EmailMessageForm
    success_url = reverse_lazy('email_message_detail')



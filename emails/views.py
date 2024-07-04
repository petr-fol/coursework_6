from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from emails.forms import EmailForm
from emails.models import Email


# Create your views here.


class EmailCreateView(CreateView):
    model = Email
    form_class = EmailForm
    context_object_name = 'email_create'


class EmailListView(ListView):
    model = Email
    context_object_name = 'emails'


class EmailDetailView(DetailView):
    model = Email
    context_object_name = 'email'


class EmailUpdateView(UpdateView):
    model = Email
    form_class = EmailForm


class EmailDeleteView(DeleteView):
    model = Email
    form_class = EmailForm


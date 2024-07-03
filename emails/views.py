from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from emails.forms import EmailForm
from emails.models import Email


# Create your views here.


class EmailCreateView(CreateView):
    template_name = 'email_create.html'
    model = Email
    form_class = EmailForm


class EmailListView(ListView):
    model = Email
    template_name = 'email_list.html'
    context_object_name = 'emails'


class EmailDetailView(DetailView):
    template_name = 'email_detail.html'
    model = Email
    context_object_name = 'email'


class EmailUpdateView(UpdateView):
    template_name = 'email_update.html'
    model = Email
    form_class = EmailForm


class EmailDeleteView(DeleteView):
    template_name = 'email_delete.html'
    model = Email
    form_class = EmailForm


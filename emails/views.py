from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from emails.forms import EmailsForm


# Create your views here.


class EmailListView(ListView):
    template_name = 'emails/email_list.html'
    context_object_name = 'emails'


class EmailDetailView(DetailView):
    template_name = 'emails/emails_detail.html'
    context_object_name = 'email'


class EmailUpdateView(UpdateView):
    template_name = 'emails/email_update.html'
    form_class = EmailsForm


class EmailDeleteView(DeleteView):
    template_name = 'emails/email_delete.html'
    form_class = EmailsForm


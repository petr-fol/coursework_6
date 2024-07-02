from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


# Create your views here.


class EmailsListView(ListView):
    template_name = 'emails/emails_list.html'


class EmailsDetailView(DetailView):
    template_name = 'emails/emails_detail.html'


class EmailsUpdateView(UpdateView):
    template_name = 'emails/emails_update.html'


class EmailsDeleteView(DeleteView):
    template_name = 'emails/emails_delete.html'


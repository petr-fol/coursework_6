from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from messages.forms import MessageForm
from messages.models import Message


# Create your views here.
class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm


class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'


class MessageDetailView(DetailView):
    model = Message
    context_object_name = 'message'


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm


class MessageDeleteView(DeleteView):
    model = Message
    form_class = MessageForm


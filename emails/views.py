from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

from emails.forms import EmailForm
from rest_framework import viewsets
from .models import EmailMessage, Attempt
from .serializers import EmailMessageSerializer, AttemptSerializer
from django.views.generic import ListView
from .models import Email
from clients.models import Client
from blog.models import Message
from .services import get_cached_statistics, get_cached_random_articles


# Create your views here.


class EmailCreateView(CreateView):
    model = Email
    form_class = EmailForm
    context_object_name = 'email_create'
    success_url = reverse_lazy('email_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class EmailListView(ListView):
    model = Email
    context_object_name = 'emails'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        statistics = get_cached_statistics()
        context.update(statistics)
        context['random_articles'] = get_cached_random_articles()
        return context


class EmailDetailView(DetailView):
    model = Email
    context_object_name = 'email'


class EmailUpdateView(UpdateView):
    model = Email
    form_class = EmailForm
    success_url = reverse_lazy('email_list')


class EmailDeleteView(DeleteView):
    model = Email
    form_class = EmailForm
    success_url = reverse_lazy('email_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not (request.user.has_perm('emails.delete_email') or
                request.user == self.object.owner or
                request.user.is_superuser):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer


class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer


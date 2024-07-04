from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from clients.forms import ClientForm
from clients.models import Client
from clients.services import cached_subjects_for_client


# Create your views here.
class ClientListView(LoginRequiredMixin,  ListView):
    model = Client
    template_name = 'clients_list.html'
    context_object_name = 'clients'
    # permission_required = 'clients.view_client'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    context_object_name = 'client'
#     permission_required = 'clients.view_client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
#     permission_required = 'clients.add_client'

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'slug': self.object.slug})


class ClientUpdateView(LoginRequiredMixin,  UpdateView):
    model = Client
    form_class = ClientForm
#     permission_required = 'clients.change_client'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Client, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')
#     permission_required = 'clients.delete_client'

    # def test_func(self):
    #     return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)

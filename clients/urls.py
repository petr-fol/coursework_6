from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.cache import cache_page

from clients.views import ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView, ClientCreateView

urlpatterns = [
    path('', cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('detail/<slug:slug>/', ClientDetailView.as_view(), name='client_detail'),
    path('edit/<slug:slug>/', ClientUpdateView.as_view(), name='client_form'),
    path('confirm_delete/<pk>/', ClientDeleteView.as_view(), name='client_confirm_delete'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

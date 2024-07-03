from django.urls import path, include

from emails.views import EmailListView, EmailDetailView, EmailUpdateView, EmailDeleteView, EmailCreateView

urlpatterns = [
    path('', EmailListView.as_view(), name='email_list'),
    path('detail/<slug:slug>/', EmailDetailView.as_view(), name='email_detail'),
    path('edit/<slug:slug>/', EmailUpdateView.as_view(), name='email_form'),
    path('confirm_delete/<int:pk>/', EmailDeleteView.as_view(), name='email_confirm_delete'),
    path('create/', EmailCreateView.as_view(), name='email_create'),
]

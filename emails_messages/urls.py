from django.urls import path, include

from emails_messages.views import EmailMessageListView, EmailMessageDetailView, EmailMessageUpdateView, \
    EmailMessageDeleteView, EmailMessageCreateView

urlpatterns = [
    path('', EmailMessageListView.as_view(), name='email_message_list'),
    path('detail/<slug:slug>/', EmailMessageDetailView.as_view(), name='email_message_detail'),
    path('edit/<slug:slug>/', EmailMessageUpdateView.as_view(), name='email_message_form'),
    path('confirm_delete/<pk>/', EmailMessageDeleteView.as_view(), name='email_message_confirm_delete'),
    path('create/', EmailMessageCreateView.as_view(), name='email_message_create'),
]

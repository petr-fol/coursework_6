from django.urls import path, include

from messages.views import MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, MessageCreateView

urlpatterns = [
    path('', MessageListView.as_view(), name='message_email_list'),
    path('detail/<slug:slug>/', MessageDetailView.as_view(), name='message_detail'),
    path('edit/<slug:slug>/', MessageUpdateView.as_view(), name='message_form'),
    path('confirm_delete/<pk>/', MessageDeleteView.as_view(), name='message_confirm_delete'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
]

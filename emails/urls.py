from django.urls import path, include

from emails.views import EmailListView

urlpatterns = [
    path('', EmailListView.as_view(), name='email_list'),
]

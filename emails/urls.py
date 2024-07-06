from django.urls import path, include

from emails.views import EmailListView, EmailDetailView, EmailUpdateView, EmailDeleteView, EmailCreateView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmailMessageViewSet, AttemptViewSet
from django.views.decorators.cache import cache_page

router = DefaultRouter()
router.register(r'email_messages', EmailMessageViewSet)
router.register(r'attempts', AttemptViewSet)

urlpatterns = [
    path('', cache_page(60)(EmailListView.as_view()), name='email_list'),
    path('detail/<int:pk>/', EmailDetailView.as_view(), name='email_detail'),
    path('edit/<int:pk>/', EmailUpdateView.as_view(), name='email_form'),
    path('confirm_delete/<int:pk>/', EmailDeleteView.as_view(), name='email_confirm_delete'),
    path('create/', EmailCreateView.as_view(), name='email_create'),
    path('', include(router.urls)),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

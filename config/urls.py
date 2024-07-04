from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emails.urls')),
    path('blog/', include('blog.urls')),
    path('clients/', include('clients.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('emails_messages/', include('emails_messages.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

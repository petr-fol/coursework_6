from django.contrib import admin

from emails.models import Email, Attempt

# Register your models here.
admin.site.register(Email)
admin.site.register(Attempt)

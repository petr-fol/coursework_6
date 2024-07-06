from django.apps import AppConfig
from time import sleep


class EmailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emails'

    def ready(self):
        from emails.tasks import start_scheduler
        sleep(2)
        start_scheduler()

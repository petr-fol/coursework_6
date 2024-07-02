from django.apps import AppConfig


class EmailsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emails'
#
# class Имя_приложенияConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'имя_приложения'
#
#     def ready(self):
#          from имя_приложения.модуль_с_задачей import функция_старта
#          sleep(2)
#          функция_старта()

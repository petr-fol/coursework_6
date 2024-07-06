import itertools

from django.db import models
from slugify import slugify

from emails_messages.models import EmailMessage
from django.utils import timezone

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Email(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок', help_text='заголовок', **NULLABLE)
    message = models.ForeignKey(EmailMessage, on_delete=models.CASCADE, verbose_name='письмо', default=None)
    clients = models.ManyToManyField('clients.Client', verbose_name='получатели',
                                     help_text='выберите получателей', related_name='email_recipients')

    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец',
                              related_name='email_owner', **NULLABLE)
    start_date = models.DateTimeField(default=timezone.now, verbose_name='Дата начала',
                                      help_text=' формат например 06.07.2024 07:24:42 ')
    periodicity = models.CharField(max_length=20, choices=[
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно')
    ], default='weekly')
    status = models.CharField(max_length=20, choices=[
        ('created', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена')
    ], default='created')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def get_success_attempts(self):
        return self.attempts.filter(status='success').count()

    def get_failed_attempts(self):
        return self.attempts.filter(status='failed').count()


class Attempt(models.Model):
    mailing = models.ForeignKey(Email, on_delete=models.CASCADE, verbose_name='рассылка', default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('success', 'Успешно'),
        ('failed', 'Ошибка')
    ], default='success')
    error_message = models.TextField(null=True, blank=True)

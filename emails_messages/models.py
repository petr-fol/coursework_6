from django.db import models
import itertools

from django.db import models
from slugify import slugify


# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class EmailMessage(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма', help_text='напишите тему письма')
    description = models.TextField(verbose_name='тело письма', help_text='напишите письмо')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец',
                              related_name='email_message_owner', **NULLABLE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title

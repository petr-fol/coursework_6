from django.db import models
import itertools

from django.db import models
from slugify import slugify


# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма', help_text='напишите тему письма')
    description = models.TextField(verbose_name='тело письма', help_text='напишите письмо')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


    def __str__(self):
        return self.title
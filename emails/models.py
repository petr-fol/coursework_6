from django.db import models
import itertools

from django.db import models
from slugify import slugify


# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Email(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма', help_text='напишите тему письма')
    description = models.TextField(verbose_name='тело письма', help_text='напишите письмо', **NULLABLE)
    recipients_list = models.ManyToManyField('emails.Client', verbose_name='получатели',
                                             help_text='напишите получатели')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    message = models.ForeignKey('emails.Message', on_delete=models.CASCADE, verbose_name='письмо',
                                help_text='выберите письмо')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, separator='-')
            for x in itertools.count(1):
                if not Email.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f'{slugify(self.title)}-{x}'
        super().save(*args, **kwargs)


class Attempt(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    response = models.TextField(verbose_name='ответ сервера', help_text='ответ сервера', **NULLABLE)

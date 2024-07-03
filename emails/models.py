import itertools

from django.db import models
from slugify import slugify

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Email(models.Model):
    # message = models.ForeignKey('emails.Message', on_delete=models.CASCADE, verbose_name='письмо')
    recipient_list = models.ManyToManyField('clients.Client', verbose_name='получатели',
                                            help_text='выберите получателей', related_name='email_recipients')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    # message = models.ForeignKey('emails.Message', on_delete=models.CASCADE, verbose_name='письмо',
    #                             help_text='выберите письмо')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец',
                              related_name='email_owner')

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

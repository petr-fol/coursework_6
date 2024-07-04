import itertools

from django.db import models
from django.db.models import EmailField

from slugify import slugify

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    email_client = models.EmailField(max_length=150, verbose_name='почта', help_text='напишите почту')
    name = models.CharField(max_length=150, verbose_name='ФИО', help_text='напишите ФИО')
    comment = models.TextField(verbose_name='комментарии', help_text='напишите комментарий', **NULLABLE)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец',
                              related_name='client_owner', **NULLABLE)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, separator='-')
            for x in itertools.count(1):
                if not Client.objects.filter(slug=self.slug).exists():
                    break
                self.slug = f'{slugify(self.name)}-{x}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name, self.email_client}"


# class Subject(models.Model):
#
#     title = models.CharField(max_length=150, verbose_name='название')
#     description = models.TextField(verbose_name='описание')
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
#
#     def __str__(self):
#         return f'{self.title}'
#
#     class Meta:
#         verbose_name = 'предмет'
#         verbose_name_plural = 'предметы'

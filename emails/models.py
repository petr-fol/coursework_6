from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Emails(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок', help_text='напишите заголовок')
    description = models.TextField(verbose_name='описание', help_text='напишите описание', **NULLABLE)
    recipients_list =
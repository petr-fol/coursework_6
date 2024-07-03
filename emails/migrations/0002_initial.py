# Generated by Django 5.0.2 on 2024-07-03 19:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_client_remove_subject_student_delete_student_and_more'),
        ('emails', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_owner', to=settings.AUTH_USER_MODEL, verbose_name='владелец'),
        ),
        migrations.AddField(
            model_name='email',
            name='recipient_list',
            field=models.ManyToManyField(help_text='выберите получателей', related_name='email_recipients', to='clients.client', verbose_name='получатели'),
        ),
    ]

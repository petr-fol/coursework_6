from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from emails.models import Email, Attempt


def send_mailing():
    current_time = timezone.now()
    mailings_to_send = Email.objects.filter(
        start_date__lte=current_time,
        status='running'
    )

    for mailing in mailings_to_send:
        for client in mailing.clients.all():
            try:
                send_mail(
                    subject=mailing.message.title,
                    message=mailing.message.description,
                    from_email='your_email@gmail.com',
                    recipient_list=[client.email_client],
                    fail_silently=False,
                )

                # Создаем успешную попытку
                Attempt.objects.create(
                    mailing=mailing,
                    status='success'
                )
            except Exception as e:
                # Сохраняем информацию об ошибке
                Attempt.objects.create(
                    mailing=mailing,
                    status='failed',
                    error_message=str(e)
                )

        # Обновляем дату следующей отправки в зависимости от периодичности
        if mailing.periodicity == 'daily':
            mailing.start_date += timezone.timedelta(days=1)
        elif mailing.periodicity == 'weekly':
            mailing.start_date += timezone.timedelta(weeks=1)
        elif mailing.periodicity == 'monthly':
            mailing.start_date += timezone.timedelta(days=30)  # Примерно месяц
        mailing.save()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing, 'interval', minutes=5)
    scheduler.start()

from django.conf import settings
from django.core.cache import cache
from .models import Email
from clients.models import Client
from blog.models import Message


def get_cached_statistics():
    if settings.CACHE_ENABLED:
        key = 'email_statistics'
        statistics = cache.get(key)
        if statistics is None:
            statistics = {
                'total_mailings': Email.objects.count(),
                'active_mailings': Email.objects.filter(status='running').count(),
                'unique_clients': Client.objects.count(),
            }
            cache.set(key, statistics, 60 * 15)  # кешируем на 15 минут
    else:
        statistics = {
            'total_mailings': Email.objects.count(),
            'active_mailings': Email.objects.filter(status='running').count(),
            'unique_clients': Client.objects.count(),
        }
    return statistics


def get_cached_random_articles():
    if settings.CACHE_ENABLED:
        key = 'random_articles'
        articles = cache.get(key)
        if articles is None:
            articles = list(Message.objects.filter(is_published=True).order_by('?')[:3])
            cache.set(key, articles, 60 * 15)  # кешируем на 15 минут
    else:
        articles = list(Message.objects.filter(is_published=True).order_by('?')[:3])
    return articles
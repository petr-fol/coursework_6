from django.conf import settings
from django.core.cache import cache



def cached_subjects_for_client(client_pk):
    if settings.CACHE_ENABLED:
        key = f'subject_list_{client_pk}'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Subject.objects.filter(client__pk=client_pk)
            cache.set(key, subject_list)
    else:
        subject_list = Subject.objects.filter(client__pk=client_pk)

    return subject_list

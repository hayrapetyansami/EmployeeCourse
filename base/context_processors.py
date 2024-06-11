from django.conf import settings


def languages(request):
    return {'LANGUAGES': settings.LANGUAGES}

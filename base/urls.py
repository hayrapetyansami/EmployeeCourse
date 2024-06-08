# base/urls.py

from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('set-language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('', include('employees.urls')),
    path('api/', include('api.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

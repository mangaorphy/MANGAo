from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import diagnose_plant


urlpatterns = [
    path('diagnose/', diagnose_plant, name='diagnose_plant'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

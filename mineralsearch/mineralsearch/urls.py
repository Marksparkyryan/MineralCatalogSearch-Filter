from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('mineralsearchapp.urls', namespace='mineralsearch')),
    url(r'.well-known/acme-challenge/', views.challenge),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

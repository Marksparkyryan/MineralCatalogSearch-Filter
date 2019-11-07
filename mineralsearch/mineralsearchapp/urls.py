# mineralsearch/mineralsearchapp/urls.py

from django.conf.urls import url
from . import views

app_name='mineralsearch'

urlpatterns = [
    url(r'index/$', views.index , name='index'),
    url(r'detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'letter/(?P<letter>[a-z]{1})', views.firstletter, name='firstletter'),
    url(r'search/', views.search, name='search'),
]


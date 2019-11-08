# mineralsearch/mineralsearchapp/urls.py

from django.conf.urls import url
from . import views

app_name='mineralsearch'

urlpatterns = [
    url(r'detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'letter/(?P<letter>[a-z]{1})?', views.letter, name='letter'),
    url(r'^$', views.letter, name='home'),
    url(r'search/', views.search, name='search'),
    url(r'group/(?P<group>[\w-]+)', views.group, name='group'),
    url(r'colour/(?P<colour>[\w-]+)', views.colour, name='colour'),
    url(r'random/', views.random, name='random'),
]


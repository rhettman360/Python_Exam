from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<userid>\d+)/add$', views.add),
    url(r'^(?P<userid>\d+)/remove$', views.remove),
    url(r'^(?P<userid>\d+)/show$', views.show),
]

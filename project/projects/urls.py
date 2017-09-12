"""Defines url patterns for Projects."""

from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
]

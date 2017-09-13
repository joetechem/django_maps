"""Defines url patterns for Projects."""

from django.conf.urls import url, include

from . import views

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
    
    # Show all Topics
    url(r'^topics/$', views.topics, name ='topics'),
    
    # Detail page for a single topic.
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]

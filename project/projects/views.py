# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
	"""The home page for Project"""
	return render(request, 'projects/index.html')
	
# The topics() function has one parameter: 
# the request object Django receieved from the server.
def topics(request):
	"""Show all topics."""
	# Querying the db by asking for the Topic objects, sorted by the date_added attribute
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'projects/topics.html', context)
	
# The topic() function gets the topic and all associated entries from the db.
def topic(request, topic_id):
	"""Show a single topic and all of its entries."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'projects/topic.html', context)

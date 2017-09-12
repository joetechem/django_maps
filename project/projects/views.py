# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
	"""The home page for Project"""
	return render(request, 'projects/index.html')
	
def topics(request):
	"""Show all topics."""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'projects/topics.html', context)

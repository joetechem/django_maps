# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm, EntryForm

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
	
#login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projects:topics'))

    context = {'form': form}
    return render(request, 'projects/new_topic.html', context)
    
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
#    if topic.owner != request.user:
#        raise Http404
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()        
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('projects:topic',
                                        args=[topic_id]))
    
    context = {'topic': topic, 'form': form}
    return render(request, 'projects/new_entry.html', context)
    
	
# The topic() function gets the topic and all associated entries from the db.
def topic(request, topic_id):
	"""Show a single topic and all of its entries."""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'projects/topic.html', context)

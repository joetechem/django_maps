from django import forms

from .models import Topic, Entry
# Form = any page that lets a user enter and submit info on a web page
# The simplest way to build a form in Django is to use a ModelForm,
# which uses the info from the models to automatically build a form.
class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}
		
# More customized then TopicForm, form creation associated with the Entry model
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

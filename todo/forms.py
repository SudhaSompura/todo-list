from django import forms
from django.utils import timezone

from .models import Task

class TaskForm(forms.Form):
	todo_text = forms.CharField(max_length=100,
		widget=forms.TextInput(
			attrs={'class':'todo_text', 'placeholder':'Enter some to-do text e.g., Delete junk files', 'autofocus':'autofocus'}
			))
	
class NewTaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['todo_text']
		widgets = {
			'todo_text' : forms.TextInput(
			attrs={'class':'todo_text', 'placeholder':'Enter some to-do text e.g., Delete junk files', 'autofocus':'autofocus'}
			)
		}
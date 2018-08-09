from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Task
from .forms import TaskForm, NewTaskForm


def index(request):
	tasks = Task.objects.order_by('id')
	#form = TaskForm()
	new_form = NewTaskForm()

	context = {'tasks':tasks, 'form' : new_form}

	return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
	import pdb; pdb.set_trace()

	new_taskform = NewTaskForm(request.POST)

	if new_taskform.is_valid():
		print("Valid Data")
		#new_task = Task(todo_text=form.cleaned_data['todo_text'])
		#new_task.save()
		new_todo = new_taskform.save()
	else:
		print("invalid data")
	return redirect('index')

def completeTodo(request, todo_id):
	todo = Task.objects.get(pk=todo_id)
	todo.task_done = True
	todo.save()

	return redirect('index')

def deleteCompleted(request):
	Task.objects.filter(task_done__exact=True).delete()
	return redirect('index')

def deleteAll(request):
	Task.objects.all().delete()
	return redirect('index')

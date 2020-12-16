from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class newTaskForm(forms.Form):
  task = forms.CharField(label='New Task')

tasks = [
  'foo',
  'abc',
  'gpp'
]

def index(request):
  if 'tasks' not in request.session:
    request.session['tasks'] = []

  context = {
    'tasks': request.session['tasks']
  }
  return render(request, 'task/index.html', context)

def addtask(request):
  if request.method == "POST":
    form = newTaskForm(request.POST) # get all form data
    if form.is_valid():
      task = form.cleaned_data['task'] # get only task data
      # tasks.append(task)
      request.session['tasks'] += [task] # adding task to the session table
      return HttpResponseRedirect(reverse('task:index'))
    else:
      context = {
        'form': form
      }
      return render(request, 'task/addtask.html', context)

  context = {
    'form': newTaskForm()
  }
  return render(request, 'task/addtask.html', context)
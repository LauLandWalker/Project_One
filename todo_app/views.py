from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from todo_app.models import TaskModel


class ListTask(ListView):
    model = TaskModel
    template_name = 'todo_app/task-list.html'
    context_object_name = 'tasks'

from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from todo_app.models import TaskModel
from todo_app.forms import TaskForm


class ListTask(ListView):
    model = TaskModel
    template_name = 'todo_app/task-list.html'
    context_object_name = 'tasks'


class CreateNewTask(CreateView):
    model = TaskModel
    template_name = 'todo_app/task-create.html'
    success_url = '/todo/'
    form_class = TaskForm


class DeleteTask(DeleteView):
    model = TaskModel
    template_name = 'todo_app/task-delete.html'
    success_url = '/todo/'


class UpdateTask(UpdateView):
    model = TaskModel
    template_name = 'todo_app/task-update.html'
    form_class = TaskForm
    success_url = '/todo/'
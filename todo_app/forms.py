from django import forms
from todo_app.models import TaskModel


class TaskForm(forms.ModelForm):
    # task_name = forms.CharField(max_length=128)

    class Meta:
        model = TaskModel
        fields = ('task_name', 'task_status')
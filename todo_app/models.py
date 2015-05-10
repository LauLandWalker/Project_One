from django.db import models


class TaskModel(models.Model):
    task_name = models.CharField(max_length=128)
    task_datetime = models.DateTimeField(auto_now_add=True)

    # task status
    status = (
        ('NOT DONE', 'not done'),
        ('DONE', 'done'),
    )

    task_status = models.CharField(choices=status, max_length=128, default=status[0])

    def __str__(self):
        return self.task_name
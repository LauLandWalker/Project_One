# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('task_name', models.CharField(max_length=128)),
                ('task_datetime', models.DateTimeField(auto_now_add=True)),
                ('task_status', models.CharField(choices=[('NOT DONE', 'not done'), ('DONE', 'done')], max_length=128, default=('NOT DONE', 'not done'))),
            ],
        ),
    ]

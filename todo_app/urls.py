from django.conf.urls import patterns, url
from todo_app import views


urlpatterns = patterns('',
                       url(r'^$', views.ListTask.as_view(), name='list-task'),
                       )
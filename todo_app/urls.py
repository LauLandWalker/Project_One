from django.conf.urls import patterns, url
from todo_app import views


urlpatterns = patterns('',
                       url(r'^$', views.ListTask.as_view(), name='list-task'),
                       url(r'^create/$', views.CreateNewTask.as_view(), name='create-task'),
                       url(r'^delete/(?P<pk>\d+)/$', views.DeleteTask.as_view(), name='delete-task'),
                       url(r'^update/(?P<pk>\d+)/$', views.UpdateTask.as_view(), name='update-task'),

                       )
from django.urls import path

from taskapp import views

app_name = 'taskapp'

urlpatterns = [
    path('create/', views.create_task_view, name='create-task-view'),

]
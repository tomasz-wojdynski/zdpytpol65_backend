from django.urls import path

from taskapp import views

app_name = 'taskapp'

urlpatterns = [
    # C
    path('create/', views.task_create_view, name='task-create-view'),

    # R
    path('', views.task_list_view, name='task-list-view'),
    path('<int:task_id>/', views.task_detail_view, name='task-detail-view'),

    # U
    path('<int:task_id>/update/', views.task_update_view, name='task-update-view'),

    # D
    path('<int:task_id>/delete/', views.task_delete_view, name='task-delete-view')
]
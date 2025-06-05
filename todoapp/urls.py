from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('tasks/<int:task_id>/detail/', views.task_detail, name='task_detail'),
]

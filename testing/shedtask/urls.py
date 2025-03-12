from django.urls import path
from .views import schedule_task, task_list

urlpatterns = [
    path('schedule/', schedule_task, name='schedule_task'),
    path('tasks/', task_list, name='task_list'),
]

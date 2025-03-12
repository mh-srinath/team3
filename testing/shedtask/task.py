from celery import shared_task
from django.utils.timezone import now
from .models import TaskScheduler

@shared_task
def check_scheduled_tasks():
    tasks = TaskScheduler.objects.filter(execution_time__lte=now())
    for task in tasks:
        task.execute_function()
        task.delete()  # Remove task after execution

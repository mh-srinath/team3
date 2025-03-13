from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now
from django.contrib import messages
from .models import TaskScheduler, ModelOne, ModelTwo, ModelThree
from .forms import TaskSchedulerForm

def schedule_task(request):
    if request.method == 'POST':
        form = TaskSchedulerForm(request.POST)
        if form.is_valid():
            model_name = form.cleaned_data['model_name']
            object_id = form.cleaned_data['object_id']
            execution_time = form.cleaned_data['execution_time']

            print("Model Name:", model_name)
            print("Object ID:", object_id)

            model_class = {'ModelOne': ModelOne, 'ModelTwo': ModelTwo, 'ModelThree': ModelThree}.get(model_name)

            if not model_class:
                messages.error(request, "Invalid Model Name")
                return redirect('schedule_task')

           # Check if object exists
            if not model_class.objects.filter(id=object_id).exists():
                messages.error(request, "Invalid Object ID")
                return redirect('schedule_task')

            # Create task
            TaskScheduler.objects.create(
                content_type=ContentType.objects.get_for_model(model_class),
                object_id=object_id,
                execution_time=execution_time
            )

            messages.success(request, "Task scheduled successfully!")
            return redirect('task_list')

    else:
        form = TaskSchedulerForm()

    return render(request, 'schedule_task.html', {'form': form})



def task_list(request):
    tasks = TaskScheduler.objects.filter(execution_time__gte=now()).order_by('execution_time')
    return render(request, 'task_list.html', {'tasks': tasks})

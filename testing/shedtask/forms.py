from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import TaskScheduler, ModelOne, ModelTwo, ModelThree

class TaskSchedulerForm(forms.ModelForm):
    model_choices = [
        ('ModelOne', 'Model One'),
        ('ModelTwo', 'Model Two'),
        ('ModelThree', 'Model Three'),
    ]
    
    model_name = forms.ChoiceField(choices=model_choices, label="Model Type")
    object_id = forms.IntegerField(label="Object ID")
    execution_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = TaskScheduler
        fields = ['model_name', 'object_id', 'execution_time']

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

    def clean(self):
        cleaned_data = super().clean()
        model_name = cleaned_data.get('model_name')
        object_id = cleaned_data.get('object_id')

        if not object_id:
            raise forms.ValidationError("Object ID is required.")

        model_class = {'ModelOne': ModelOne, 'ModelTwo': ModelTwo, 'ModelThree': ModelThree}.get(model_name)

        if not model_class:
            raise forms.ValidationError("Invalid model selection.")

        # Check if the object ID exists in the selected model
        if not model_class.objects.filter(id=object_id).exists():
            raise forms.ValidationError(f"Invalid Object ID: {object_id} does not exist in {model_name}.")

        return cleaned_data

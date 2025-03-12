from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now
from celery import shared_task

# Model One
class ModelOne(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @shared_task
    def custom_function(self):
        print(f"Executing ModelOne function for {self.name}")


# Model Two
class ModelTwo(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @shared_task
    def custom_function(self):
        print(f"Executing ModelTwo function for {self.name}")


# Model Three
class ModelThree(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @shared_task
    def custom_function(self):
        print(f"Executing ModelThree function for {self.name}")


# Task Scheduler with Generic Foreign Key
class TaskScheduler(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # Dynamic relation
    object_id = models.PositiveIntegerField()
    target_object = GenericForeignKey('content_type', 'object_id')  # Allows dynamic model reference

    execution_time = models.DateTimeField()
    status = models.BooleanField(default=False)  # False = pending, True = executed

    def __str__(self):
        return f"Task for {self.content_type} at {self.execution_time}"

    def execute_function(self):
        """ Calls the custom function of the associated model instance. """
        if hasattr(self.target_object, 'custom_function'):
            self.target_object.custom_function.delay()  # Executes as Celery task

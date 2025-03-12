from django.contrib import admin
from .models import ModelOne, ModelTwo, ModelThree, TaskScheduler

admin.site.register(ModelOne)
admin.site.register(ModelTwo)
admin.site.register(ModelThree)
admin.site.register(TaskScheduler)

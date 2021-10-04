from django.contrib import admin
from .models import *
from .management.commands.bot import TaskAdmin


admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(TaskList)
admin.site.register(Task, TaskAdmin)

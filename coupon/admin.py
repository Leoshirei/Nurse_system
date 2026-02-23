from django.contrib import admin
from .models import Patient, Medical_Task, Habit_Table, Task_Status
# Register your models here.
admin.site.register(Patient)
admin.site.register(Medical_Task)
admin.site.register(Habit_Table)
admin.site.register(Task_Status)
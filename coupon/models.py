from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    pesel = models.CharField(max_length = 11)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.name + " " + self.surname + " " + self.pesel

class Medical_Task(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Habit_Table(models.Model):
    person = models.ForeignKey(Patient, on_delete = models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()

class Task_Status(models.Model):
    table = models.ForeignKey(Habit_Table, on_delete=models.CASCADE)
    habit = models.ForeignKey(Medical_Task, on_delete=models.CASCADE)
    date = models.DateField()
    done = models.BooleanField(default=False)


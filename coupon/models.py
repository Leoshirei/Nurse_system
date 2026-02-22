from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Nurse(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    def __str__(self):
        return self.name + " " + self.surname
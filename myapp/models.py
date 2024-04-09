from django.db import models

class todoitem(models.Model):
    title=models.CharField(max_length=255)
    completed=models.BooleanField(default=False)

class users(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
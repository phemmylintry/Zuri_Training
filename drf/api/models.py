from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    reg_no = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
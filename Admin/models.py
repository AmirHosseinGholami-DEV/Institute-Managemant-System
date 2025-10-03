from django.db import models

class Student_Database(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=30)
    number = models.CharField(max_length=50)
    Amount = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

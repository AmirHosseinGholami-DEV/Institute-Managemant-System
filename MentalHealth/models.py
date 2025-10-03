from django.db import models

class Mental_Health_Database(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, default='')
    def __str__(self):
        return self.name

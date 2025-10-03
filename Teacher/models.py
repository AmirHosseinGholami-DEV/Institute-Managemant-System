from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=70)
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name
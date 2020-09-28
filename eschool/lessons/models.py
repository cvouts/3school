from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Lesson(models.Model):
    name = models.CharField(max_length=200)
    id = models.IntegerField
    teacher = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="No Teacher")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lesson-detail', args=[str(self.id)])
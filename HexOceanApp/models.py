from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    image = models.ImageField(upload_to='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

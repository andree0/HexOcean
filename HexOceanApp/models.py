from django.db import models
from django.contrib.auth.models import User

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases

saved_file.connect(generate_aliases)


class Photo(models.Model):
    image = ThumbnailerImageField(upload_to='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url

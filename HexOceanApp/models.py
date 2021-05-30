from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission, User

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases

saved_file.connect(generate_aliases)


class Photo(models.Model):
    image = ThumbnailerImageField(upload_to='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url


# Creates user's new group 'Basic' if it doesn't exist
# and sets permissions for its
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        basic = Group.objects.get_or_create(name='Basic')
        if not basic[0].permissions.all():
            add_photo = Permission.objects.get(codename="add_photo")
            view_thumbnail = Permission.objects.get(codename="view_thumbnail")
            basic[0].permissions.add(add_photo, view_thumbnail, )
        if not instance.is_staff and not instance.is_superuser:
            instance.groups.add(basic[0].pk)


from django.contrib import admin

from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.widgets import ImageClearableFileInput

from HexOceanApp.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ('image', 'owner', )
    formfield_overrides = {
        ThumbnailerImageField: {'widget': ImageClearableFileInput},
    }

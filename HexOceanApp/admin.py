from django.contrib import admin

from HexOceanApp.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ('image', 'user', )

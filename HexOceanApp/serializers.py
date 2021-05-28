from easy_thumbnails_rest.serializers import ThumbnailerJSONSerializer
from rest_framework import serializers

from HexOcean.settings import THUMBNAIL_ALIASES
from HexOceanApp.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    image = ThumbnailerJSONSerializer(alias="")

    class Meta:
        model = Photo
        fields = ('id', 'image', 'owner', )
        read_only_fields = ('id', 'owner', )


class BasicPhotoSerializer(PhotoSerializer):
    small_thumbnail = serializers.SerializerMethodField()

    @staticmethod
    def get_small_thumbnail(obj):
        options = THUMBNAIL_ALIASES[""]["small_thumbnail"]
        return obj.image.get_thumbnail(options).url

    class Meta:
        model = Photo
        fields = ('id', 'small_thumbnail', 'owner', )
        read_only_fields = ('id', 'owner',)


# class EnterprisePhotoSerializer(PhotoSerializer):

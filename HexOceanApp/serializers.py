from easy_thumbnails_rest.serializers import ThumbnailerJSONSerializer
from rest_framework import serializers

from HexOceanApp.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = ThumbnailerJSONSerializer(alias="")

    class Meta:
        model = Photo
        fields = ('id', 'image', 'owner', )
        read_only_fields = ('id', 'owner', )


class GroupBasicPhoto(PhotoSerializer):
    image = ThumbnailerJSONSerializer(alias='basic')

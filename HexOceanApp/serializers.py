from rest_framework import serializers
from HexOceanApp.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('image', 'owner', )
        read_only_fields = ('owner', )

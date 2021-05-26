from rest_framework import generics

from HexOceanApp.models import Photo
from HexOceanApp.serializers import GroupBasicPhoto, PhotoSerializer


class PhotoListView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()

    def get_serializer_class(self):
        if self.request.user.groups.filter(name="Basic"):
            return GroupBasicPhoto
        return PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        serializer.save()

    def get_queryset(self):
        user = self.request.user
        return Photo.objects.filter(owner=user).order_by('-pk')

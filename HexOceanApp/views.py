from rest_framework import generics

from HexOceanApp.models import Photo
from HexOceanApp.serializers import PhotoSerializer


class PhotoListView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Photo.objects.filter(owner=user)
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(request.POST)
    #     if serializer.is_valid():
    #         serializer.save(owner=request.user)
    #     return super().post(request, *args, **kwargs)

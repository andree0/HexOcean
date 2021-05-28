from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from HexOceanApp.models import Photo
from HexOceanApp.serializers import BasicPhotoSerializer, PhotoSerializer


class PhotoListView(generics.ListCreateAPIView):
    """
    View class for displaying a list of user's `Photo` objects and
    creating new `Photo' object using POST method.
    The default permission setting for the whole project
    is IsAuthenticated.
    """
    def get_queryset(self):
        user = self.request.user
        return Photo.objects.filter(owner=user).order_by('-pk')

    def get_serializer_class(self):
        if self.request.user.groups.filter(name="Basic") \
                and self.request.method == 'GET':
            return BasicPhotoSerializer
        return PhotoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data,
                                     context={'request': request})
        if serializer.is_valid():
            self.perform_create(serializer)
            if request.user.groups.filter(name='Basic').exists():
                serializer.data["image"][
                    "original"] = "Buy Premium or Enterprise account " \
                                  "to see this url"
                serializer.data["image"][
                    "large_thumbnail"] = "Buy Premium or Enterprise account " \
                                         "to see this url"
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

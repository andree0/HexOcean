import pytest
from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile

from HexOceanApp.models import Photo


@pytest.mark.django_db
def test_get_photo_list_view(client, user):
    client.login(username=user.username, password='strongPassword100%')
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_photo(client, user):
    client.login(username=user.username, password='strongPassword100%')
    photo_before = Photo.objects.count()
    image = Image.new('RGB', (100, 100))
    tmp_file = SimpleUploadedFile(
                      "file.jpg", b"file_content", content_type="image/jpg")
    image.save(tmp_file)
    tmp_file.seek(0)
    response = client.post('/', data={'image': tmp_file}, format="multipart")
    assert response.status_code == 201
    assert Photo.objects.count() == photo_before + 1

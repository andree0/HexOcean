import pytest

from django.test import Client

from HexOceanApp.tests.utils import create_fake_user


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user():
    return create_fake_user()

from faker import Faker
from random import randint

from django.contrib.auth.models import User

fake = Faker("en-US")


def fake_user_data():
    """Generate a dict of user data"""
    nr1 = randint(1, 100)
    nr2 = randint(1, 100)
    return {
        'username': f'user_{nr1}{nr2}_{fake.safe_color_name()}',
        'password': 'strongPassword100%',
    }


def create_fake_user():
    """Generate new fake user and save to database."""
    user_data = fake_user_data()
    return User.objects.create_user(
            username=user_data['username'],
            password=user_data['password'],
        )

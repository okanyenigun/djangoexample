import pytest
from rest_framework.test import APIClient
from resttest.models import F1Driver

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def f1driver_payload():
    payload = {
        'name': 'Lewis Hamilton',
        'team': 'Mercedes',
        'country': 'England',
        'age': 38,
        'podiums': 412,
        'championships': 7,
    }
    return payload

@pytest.fixture
def create_f1driver():
    payload = {
        'name': 'Lewis Hamilton',
        'team': 'Mercedes',
        'country': 'England',
        'age': 38,
        'podiums': 412,
        'championships': 7,
    }
    record =F1Driver.objects.create(**payload)
    return record


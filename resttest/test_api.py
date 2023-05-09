import pytest
from faker import Faker
from django.urls import reverse
from rest_framework.test import APIClient
from resttest.models import F1Driver
from rest_framework import status
from resttest.serializers import F1DriverSerializer

def test_pytest_working():
    assert True == True

client = APIClient()

@pytest.mark.django_db
def test_create_f1driver():
    response = client.post('/api/create-f1driver/')
    assert response.status_code == 201
    f1driver = F1Driver.objects.first()
    assert f1driver is not None

@pytest.mark.django_db
def test_create_f1driver_payload():
    client = APIClient()
    url = '/api/create-f1driver/'
    payload = {
        'name': 'Lewis Hamilton',
        'team': 'Mercedes',
        'country': 'England',
        'age': '38',
        'podiums': 412,
        'championships': 7,
    }
    response = client.post(url, payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert F1Driver.objects.count() == 1

@pytest.mark.django_db
def test_create_f1driver_fixture(api_client, f1driver_payload):
    url = '/api/create-f1driver/'
    response = api_client.post(url, f1driver_payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert F1Driver.objects.count() == 1

@pytest.mark.django_db
def test_get_f1drivers(api_client, create_f1driver):
    response = api_client.get(reverse('f1driver-list'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    f1driver_data = dict(response.data[0]) 
    assert f1driver_data['name'] == create_f1driver.name
    assert f1driver_data['team'] == create_f1driver.team
    assert f1driver_data['country'] == create_f1driver.country
    assert f1driver_data['age'] == create_f1driver.age
    assert f1driver_data['podiums'] == create_f1driver.podiums
    assert f1driver_data['championships'] == create_f1driver.championships

fake = Faker()
@pytest.mark.django_db
def test_update_f1driver(create_f1driver):
    # Create a new F1 driver record to update

    # Define the update payload
    payload = {
        "name": fake.name(),
        "team": fake.company(),
        "country": fake.country(),
        "age": fake.random_int(min=18, max=50),
        "podiums": fake.random_int(min=0, max=100),
        "championships": fake.random_int(min=0, max=10)
    }

    # Update the record using the REST API
    client = APIClient()
    response = client.put(f'/api/f1drivers/{create_f1driver.id}/', payload, format='json')

     # Check that the response has a 200 OK status code
    assert response.status_code == 200

    # Reload the F1 driver record from the database to check that it has been updated
    create_f1driver.refresh_from_db()

    # Check that the F1 driver record has been updated with the correct values
    assert create_f1driver.name == payload['name']
    assert create_f1driver.team == payload['team']
    assert create_f1driver.country == payload['country']
    assert create_f1driver.age == payload['age']
    assert create_f1driver.podiums == payload['podiums']
    assert create_f1driver.championships == payload['championships']

    # Check that the serialized response data matches the updated record
    serializer = F1DriverSerializer(create_f1driver)
    assert response.data == serializer.data


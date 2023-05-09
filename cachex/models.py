from django.db import models
from faker import Faker
fake = Faker()

class DummyModel(models.Model):
    name = models.CharField(max_length=100, default=fake.name)
    email = models.EmailField(max_length=100, default=fake.email)
    address = models.CharField(max_length=100, default=fake.address)
    phone_number = models.CharField(max_length=20, default=fake.phone_number)

    def __str__(self):
        return self.name
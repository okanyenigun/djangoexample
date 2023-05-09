from django.db import models
from faker import Faker

fake = Faker()

class F1Driver(models.Model):
    name = models.CharField(max_length=50, default=fake.name)
    team = models.CharField(max_length=50, default=fake.random_element(elements=('Mercedes', 'Ferrari', 'Red Bull')))
    country = models.CharField(max_length=50, default=fake.country)
    age = models.PositiveIntegerField(default=fake.random_int(min=18, max=45))
    podiums = models.PositiveIntegerField(default=fake.random_int(min=0, max=100))
    championships = models.PositiveIntegerField(default=fake.random_int(min=0, max=5))
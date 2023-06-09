# Generated by Django 4.1.7 on 2023-04-01 21:13

from django.db import migrations, models
import faker.providers.address
import faker.providers.internet
import faker.providers.person
import faker.providers.phone_number


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=faker.providers.person.Provider.name, max_length=100)),
                ('email', models.EmailField(default=faker.providers.internet.Provider.email, max_length=100)),
                ('address', models.CharField(default=faker.providers.address.Provider.address, max_length=100)),
                ('phone_number', models.CharField(default=faker.providers.phone_number.Provider.phone_number, max_length=20)),
            ],
        ),
    ]

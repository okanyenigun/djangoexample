# Generated by Django 4.1.7 on 2023-04-02 21:01

from django.db import migrations, models
import faker.providers.address
import faker.providers.internet
import faker.providers.person
import faker.providers.phone_number


class Migration(migrations.Migration):

    dependencies = [
        ('cachex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummymodel',
            name='address',
            field=models.CharField(default=faker.providers.address.Provider.address, max_length=100),
        ),
        migrations.AlterField(
            model_name='dummymodel',
            name='email',
            field=models.EmailField(default=faker.providers.internet.Provider.email, max_length=100),
        ),
        migrations.AlterField(
            model_name='dummymodel',
            name='name',
            field=models.CharField(default=faker.providers.person.Provider.name, max_length=100),
        ),
        migrations.AlterField(
            model_name='dummymodel',
            name='phone_number',
            field=models.CharField(default=faker.providers.phone_number.Provider.phone_number, max_length=20),
        ),
    ]

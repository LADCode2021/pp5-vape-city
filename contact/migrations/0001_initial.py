# Generated by Django 3.2 on 2023-03-13 22:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email_address', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11, message='Please enter valid phone number starting with 0')])),
                ('comments', models.TextField()),
            ],
        ),
    ]
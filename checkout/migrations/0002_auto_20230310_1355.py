# Generated by Django 3.2 on 2023-03-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='product_strength',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_flavour',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

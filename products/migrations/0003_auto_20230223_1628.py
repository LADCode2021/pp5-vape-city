# Generated by Django 3.2 on 2023-02-23 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230223_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour', models.CharField(blank=True, max_length=254, null=True)),
                ('strength', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='flavours',
        ),
        migrations.RemoveField(
            model_name='product',
            name='strength',
        ),
        migrations.DeleteModel(
            name='Flavour',
        ),
        migrations.DeleteModel(
            name='Strength',
        ),
        migrations.AddField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]

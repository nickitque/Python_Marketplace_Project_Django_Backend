# Generated by Django 4.2.7 on 2024-01-13 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0017_location_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(default='Минская обл.', max_length=255),
        ),
    ]

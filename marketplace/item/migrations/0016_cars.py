# Generated by Django 4.2.7 on 2024-01-04 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_alter_item_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]

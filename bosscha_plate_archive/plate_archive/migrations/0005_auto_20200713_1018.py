# Generated by Django 3.0.8 on 2020-07-13 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0004_auto_20200711_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plate',
            old_name='plate',
            new_name='plate_id',
        ),
    ]
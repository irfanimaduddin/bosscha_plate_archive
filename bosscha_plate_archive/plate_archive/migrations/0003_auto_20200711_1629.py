# Generated by Django 3.0.8 on 2020-07-11 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0002_auto_20200711_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='plate',
            name='plate_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

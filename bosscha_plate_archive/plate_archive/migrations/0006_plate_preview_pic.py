# Generated by Django 3.0.8 on 2020-07-14 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0005_auto_20200713_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='preview_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0014_auto_20200719_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='logbook_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-31 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0032_auto_20200824_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]

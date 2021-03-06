# Generated by Django 3.0.8 on 2020-08-23 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0022_auto_20200823_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='plate',
            name='status',
            field=models.CharField(blank=True, choices=[('Unavailable', 'Unavailable'), ('Available', 'Available'), ('Processed', 'Processed')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]

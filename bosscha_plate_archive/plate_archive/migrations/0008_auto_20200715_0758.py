# Generated by Django 3.0.8 on 2020-07-15 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0007_auto_20200715_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starobject',
            name='t_end',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='starobject',
            name='t_start',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

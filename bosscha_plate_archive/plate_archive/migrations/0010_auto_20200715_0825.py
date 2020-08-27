# Generated by Django 3.0.8 on 2020-07-15 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0009_auto_20200715_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starobject',
            name='plate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='star_object', to='plate_archive.Plate'),
        ),
    ]

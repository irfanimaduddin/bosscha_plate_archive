# Generated by Django 3.0.8 on 2020-08-23 04:38

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0029_auto_20200823_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plate',
            name='date_modified',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', when={'Processed'}),
        ),
        migrations.AlterField(
            model_name='plate',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='Unavailable', max_length=100, no_check_for_status=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-14 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0016_auto_20200813_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_id', models.CharField(blank=True, max_length=10, null=True)),
                ('meas_auth', models.CharField(blank=True, max_length=10, null=True)),
                ('meas_date', models.CharField(blank=True, default='1970-01-01', max_length=10, null=True)),
                ('cover_note', models.TextField(blank=True, null=True)),
                ('envelope', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover_id', to='plate_archive.Plate')),
            ],
        ),
        migrations.DeleteModel(
            name='ScannedLogbook',
        ),
        migrations.AlterField(
            model_name='starobject',
            name='date',
            field=models.CharField(blank=True, default='1970-01-01', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='starobject',
            name='film',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='starobject',
            name='plate_size',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Plate size (mm x mm)'),
        ),
    ]

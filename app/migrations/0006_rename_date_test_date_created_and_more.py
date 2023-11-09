# Generated by Django 4.2.6 on 2023-11-08 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_test_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='location',
            new_name='home_address',
        ),
        migrations.AddField(
            model_name='test',
            name='scheduleDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='state',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='test_id',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='test',
            name='test_option',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

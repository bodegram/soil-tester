# Generated by Django 4.2.6 on 2023-11-09 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_customuser_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_test', models.CharField(max_length=1000, null=True)),
                ('test_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.test')),
            ],
        ),
    ]

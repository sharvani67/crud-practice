# Generated by Django 5.1.3 on 2024-11-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0027_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('employee', 'Employee'), ('student', 'Student'), ('adminstaff', 'Adminstaff')], max_length=20),
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0013_remove_student_custom_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='custom_id',
            field=models.IntegerField(default=1, null=True, unique=True),
        ),
    ]

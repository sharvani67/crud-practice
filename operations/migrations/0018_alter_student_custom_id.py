# Generated by Django 5.1.3 on 2024-11-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0017_alter_student_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='custom_id',
            field=models.IntegerField(default=1, null=True, unique=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-11-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0006_alter_student_fathername_alter_student_mothername_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fathername',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='mothername',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

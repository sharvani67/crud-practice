# Generated by Django 5.1.3 on 2024-11-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0007_alter_student_fathername_alter_student_mothername_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeename', models.CharField(max_length=20)),
                ('employeeid', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=20)),
                ('startingdate', models.CharField(max_length=20)),
                ('endingdate', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]

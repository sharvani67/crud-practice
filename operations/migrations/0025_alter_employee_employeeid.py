# Generated by Django 5.1.3 on 2024-11-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0024_alter_employee_employeename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
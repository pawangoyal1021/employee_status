# Generated by Django 5.0 on 2023-12-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0006_alter_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(default='0000000', max_length=1000, null=True),
        ),
    ]
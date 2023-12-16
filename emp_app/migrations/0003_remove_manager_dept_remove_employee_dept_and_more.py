# Generated by Django 5.0 on 2023-12-16 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_manager_leave_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='hire_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Leave',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]

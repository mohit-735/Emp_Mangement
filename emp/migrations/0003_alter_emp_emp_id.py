# Generated by Django 5.1 on 2024-08-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_testimonial_rename_department_emp_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='emp_ID',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

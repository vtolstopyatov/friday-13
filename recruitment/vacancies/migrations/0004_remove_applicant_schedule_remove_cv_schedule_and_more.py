# Generated by Django 4.2.6 on 2023-10-28 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_remove_applicant_min_wage_remove_cv_min_wage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='schedule',
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-28 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagelevel',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1'), (6, 'C2')]),
        ),
    ]
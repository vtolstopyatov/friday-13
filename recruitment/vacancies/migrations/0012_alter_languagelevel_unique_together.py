# Generated by Django 4.2.6 on 2023-10-30 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0011_alter_languagelevel_level_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='languagelevel',
            unique_together=set(),
        ),
    ]
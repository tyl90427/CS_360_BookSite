# Generated by Django 3.1 on 2020-10-20 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20201019_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='powerplant',
            old_name='c_co2',
            new_name='co2',
        ),
        migrations.RenameField(
            model_name='powerplant',
            old_name='c_hg',
            new_name='hg',
        ),
        migrations.RenameField(
            model_name='powerplant',
            old_name='c_no',
            new_name='nox',
        ),
    ]

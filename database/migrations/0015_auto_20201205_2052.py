# Generated by Django 3.1.1 on 2020-12-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20201205_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='general_review',
            field=models.CharField(max_length=1000),
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20201205_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='personal_reviews',
            field=models.CharField(default='Coming Soon', max_length=1500),
            preserve_default=False,
        ),
    ]
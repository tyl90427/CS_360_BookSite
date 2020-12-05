# Generated by Django 3.1 on 2020-10-18 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30, unique=True)),
                ('lat', models.CharField(max_length=30)),
                ('long', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('regmark', models.CharField(max_length=30)),
                ('temp', models.DecimalField(decimal_places=6, max_digits=7)),
                ('humidity', models.DecimalField(decimal_places=6, max_digits=7)),
                ('wind_speed', models.DecimalField(decimal_places=6, max_digits=7)),
                ('wind_direction', models.DecimalField(decimal_places=6, max_digits=7)),
                ('speed', models.DecimalField(decimal_places=6, max_digits=7)),
                ('accuracy', models.DecimalField(decimal_places=6, max_digits=7)),
                ('c_co', models.DecimalField(decimal_places=6, max_digits=7)),
                ('c_co2', models.DecimalField(decimal_places=6, max_digits=7)),
                ('c_hc', models.DecimalField(decimal_places=6, max_digits=7)),
                ('c_no', models.DecimalField(decimal_places=6, max_digits=7)),
                ('efco', models.DecimalField(decimal_places=6, max_digits=7)),
                ('efhc', models.DecimalField(decimal_places=6, max_digits=7)),
                ('efno', models.DecimalField(decimal_places=6, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_family', models.CharField(max_length=30)),
                ('engine_code', models.CharField(max_length=30)),
                ('engine_model', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(max_length=30)),
                ('part_name', models.CharField(max_length=30)),
                ('part_desc', models.CharField(max_length=100)),
                ('part_num', models.CharField(max_length=30)),
                ('automaker', models.CharField(max_length=30)),
                ('trim', models.CharField(max_length=30)),
                ('model_year', models.CharField(max_length=10)),
                ('sensor', models.BooleanField(default=False)),
            ],
        ),
    ]
# Generated by Django 4.0.6 on 2022-08-05 17:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_alter_about_about_me'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact_us',
        ),
        migrations.AddField(
            model_name='about',
            name='facebook',
            field=models.CharField(default=datetime.datetime(2022, 8, 5, 17, 20, 8, 657350, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='instagram',
            field=models.CharField(default=datetime.datetime(2022, 8, 5, 17, 20, 17, 897646, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.CharField(default=datetime.datetime(2022, 8, 5, 17, 20, 35, 489029, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='location',
            field=models.CharField(default=datetime.datetime(2022, 8, 5, 17, 20, 41, 105713, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]

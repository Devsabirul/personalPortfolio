# Generated by Django 4.0.6 on 2022-08-04 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_testimonial_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='pic',
            new_name='photo',
        ),
    ]

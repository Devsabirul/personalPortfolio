# Generated by Django 4.0.6 on 2022-08-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_commnets_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_me',
            field=models.TextField(),
        ),
    ]
# Generated by Django 4.0.6 on 2022-11-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_portfolio_item_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_item',
            name='slider_one',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='portfolio_item',
            name='slider_three',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='portfolio_item',
            name='slider_two',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='portfolio_item',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/%y'),
        ),
    ]

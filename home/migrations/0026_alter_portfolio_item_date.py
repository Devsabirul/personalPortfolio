# Generated by Django 4.0.6 on 2022-08-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_portfolio_item_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_item',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

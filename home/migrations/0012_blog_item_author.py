# Generated by Django 4.0.6 on 2022-08-03 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_blog_blog_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_item',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_blog_item_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commnets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('domain', models.CharField(max_length=100)),
                ('comment', models.TextField()),
            ],
        ),
    ]
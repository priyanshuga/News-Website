# Generated by Django 3.0.8 on 2020-07-12 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20200712_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='twitter',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
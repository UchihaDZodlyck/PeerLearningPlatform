# Generated by Django 3.0.3 on 2020-05-11 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_like_nums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='like_nums',
        ),
    ]

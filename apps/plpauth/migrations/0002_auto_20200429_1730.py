# Generated by Django 3.0.3 on 2020-04-29 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plpauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
    ]

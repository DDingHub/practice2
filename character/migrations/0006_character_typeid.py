# Generated by Django 4.2 on 2023-08-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0005_character_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='typeId',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.2 on 2023-08-21 03:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gongmo', '0022_scrap_jjim'),
    ]

    operations = [
        migrations.AddField(
            model_name='jjim',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='scrap',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='jjim',
            unique_together={('user', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='scrap',
            unique_together={('user', 'contest')},
        ),
    ]

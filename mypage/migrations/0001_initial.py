# Generated by Django 4.2 on 2023-08-29 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('job', models.JSONField(blank=True, null=True)),
                ('hobby', models.JSONField(blank=True, null=True)),
                ('dream', models.JSONField(blank=True, null=True)),
                ('tendency_worktime', models.CharField(max_length=100)),
                ('tendency_personality', models.JSONField(blank=True, null=True)),
                ('tendency_MBTI', models.CharField(max_length=10)),
                ('languages_tools', models.JSONField(blank=True, null=True)),
                ('call', models.JSONField(blank=True, default=dict, null=True)),
                ('introduce', models.JSONField(blank=True, default=dict, null=True)),
                ('portfolio', models.JSONField(blank=True, default=dict, null=True)),
                ('user_type', models.JSONField(blank=True, default=dict, null=True)),
                ('type_message', models.JSONField(blank=True, default=dict, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

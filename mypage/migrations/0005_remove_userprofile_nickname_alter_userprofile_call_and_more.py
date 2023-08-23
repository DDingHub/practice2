# Generated by Django 4.2.4 on 2023-08-23 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mypage', '0004_userprofile_call_userprofile_dream_userprofile_hobby_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='call',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dream',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hobby',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='introduce',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='job',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='languages_tools',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='major',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='portfolio',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tendency_MBTI',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tendency_personality',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tendency_worktime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='type_message',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]

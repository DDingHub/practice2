# Generated by Django 4.2 on 2023-08-29 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.TextField()),
                ('field', models.CharField(max_length=255)),
                ('eligibility', models.CharField(max_length=255)),
                ('organizer', models.CharField(max_length=255)),
                ('sponsorship', models.CharField(max_length=255)),
                ('application_period', models.CharField(max_length=255)),
                ('prize_total', models.CharField(max_length=255)),
                ('prize_first', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('details', models.TextField()),
                ('isSchool', models.BooleanField(default=False)),
                ('registration_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('viewCount', models.PositiveIntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=100)),
                ('job', models.TextField()),
                ('hobby', models.TextField()),
                ('dream', models.TextField()),
                ('tendency_worktime', models.CharField(max_length=20)),
                ('tendency_personality', models.TextField()),
                ('tendency_MBTI', models.CharField(max_length=10)),
                ('languages_tools', models.TextField()),
                ('call', models.TextField()),
                ('introduce', models.TextField()),
                ('portfolio', models.TextField()),
                ('user_type', models.TextField()),
                ('type_message', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('teamname', models.CharField(max_length=100, null=True)),
                ('call', models.CharField(max_length=100, null=True)),
                ('detail', models.TextField(null=True)),
                ('tendency', models.JSONField(default=list)),
                ('dev_capacity', models.PositiveIntegerField(default=0)),
                ('plan_capacity', models.PositiveIntegerField(default=0)),
                ('design_capacity', models.PositiveIntegerField(default=0)),
                ('dev', models.PositiveIntegerField(default=0)),
                ('plan', models.PositiveIntegerField(default=0)),
                ('design', models.PositiveIntegerField(default=0)),
                ('jickgoon_type', models.CharField(blank=True, choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')], max_length=50)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gongmo.contest')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RejectedTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gongmo.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.TextField(null=True)),
                ('type', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jickgoon', models.CharField(choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')], max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='gongmo.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jickgoon', models.CharField(choices=[('dev', '개발'), ('plan', '기획'), ('design', '디자인')], max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gongmo.team')),
            ],
        ),
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gongmo.contest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'contest')},
            },
        ),
        migrations.CreateModel(
            name='Jjim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gongmo.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'team')},
            },
        ),
    ]

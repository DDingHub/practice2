# Generated by Django 4.2 on 2023-08-21 16:07

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
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jickgoon_type', models.CharField(choices=[('개발', '개발'), ('기획', '기획'), ('디자인', '디자인')], max_length=50)),
                ('hobbies', models.JSONField(default=list)),
                ('courses', models.JSONField(default=list)),
                ('workingTimes', models.JSONField(default=list)),
                ('characters', models.JSONField(default=list)),
                ('mbti', models.JSONField(default=list)),
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
                ('tendency', models.TextField(default='[]')),
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
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.TextField(null=True)),
                ('is_read', models.BooleanField(default=False)),
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

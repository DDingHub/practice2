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
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('type_src', models.TextField()),
                ('type_message', models.TextField()),
                ('type_hashtag', models.TextField()),
                ('type_explain1', models.TextField()),
                ('type_explain2', models.TextField()),
                ('type_explain3', models.TextField()),
                ('type_explain4', models.TextField()),
                ('type_best', models.CharField(max_length=255)),
                ('type_best_message', models.TextField()),
                ('type_best_src', models.TextField()),
                ('type_worst', models.CharField(max_length=255)),
                ('type_worst_message', models.TextField()),
                ('type_worst_src', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='r_myCharacter', to='character.character')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

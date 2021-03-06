# Generated by Django 2.1.1 on 2018-10-25 12:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='simple_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='sms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('message', models.TextField(max_length=160, unique=True)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('genre', models.CharField(choices=[('fm', 'family'), ('si', 'single')], max_length=12)),
            ],
            options={
                'verbose_name': 'sms',
            },
        ),
        migrations.CreateModel(
            name='tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('fm', 'family'), ('sx', 'sex')], max_length=12)),
                ('name', models.CharField(max_length=10, unique=True)),
                ('message', models.TextField(max_length=160, unique=True)),
                ('added_on', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete='cascade', related_name='tipowner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='voice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]

# Generated by Django 2.1.1 on 2018-10-23 09:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0005_auto_20181022_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='caller',
            field=models.OneToOneField(blank=True, null=True, on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]

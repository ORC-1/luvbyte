# Generated by Django 2.1.1 on 2018-10-18 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('luvbytes', '0005_auto_20181018_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sms',
            name='owner',
        ),
    ]
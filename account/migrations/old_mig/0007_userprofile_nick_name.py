# Generated by Django 2.1.1 on 2018-10-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_userprofile_caller'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(default='tester', max_length=8, verbose_name='Nickname'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.1 on 2018-10-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luvbytes', '0008_simple_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simple_log',
            name='message',
            field=models.TextField(max_length=200),
        ),
    ]
# Generated by Django 2.1.1 on 2018-10-18 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('luvbytes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='type',
            field=models.CharField(choices=[('fm', 'family'), ('si', 'single')], default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
    ]

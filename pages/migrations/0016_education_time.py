# Generated by Django 2.2.4 on 2019-08-29 08:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20190829_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='time',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]

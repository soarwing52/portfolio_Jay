# Generated by Django 2.2.4 on 2019-08-28 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('introduction', models.TextField()),
            ],
        ),
    ]

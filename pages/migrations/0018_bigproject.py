# Generated by Django 2.2.3 on 2019-11-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='BigProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('image', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190801_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='decription',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]

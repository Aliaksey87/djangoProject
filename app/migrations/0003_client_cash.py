# Generated by Django 3.2 on 2021-07-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cash',
            field=models.CharField(default=' ', max_length=100, verbose_name='cash'),
            preserve_default=False,
        ),
    ]

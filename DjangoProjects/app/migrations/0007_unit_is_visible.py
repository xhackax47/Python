# Generated by Django 3.1 on 2019-11-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191126_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='is_visible',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]

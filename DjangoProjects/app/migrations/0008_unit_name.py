# Generated by Django 3.1 on 2019-11-26 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_unit_is_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='name',
            field=models.CharField(blank=True, default='No Name', max_length=200, null=True),
        ),
    ]

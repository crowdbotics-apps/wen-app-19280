# Generated by Django 2.2.14 on 2020-07-31 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forwardedmessage',
            name='renatus',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]

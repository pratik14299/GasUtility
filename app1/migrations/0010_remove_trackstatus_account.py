# Generated by Django 4.2.4 on 2023-08-17 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_trackstatus_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackstatus',
            name='account',
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-17 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_servicerequest_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='account',
        ),
    ]

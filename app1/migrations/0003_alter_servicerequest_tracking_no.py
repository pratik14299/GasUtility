# Generated by Django 4.2.4 on 2023-08-17 11:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_servicerequest_account_servicerequest_tracking_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='tracking_no',
            field=models.UUIDField(verbose_name=uuid.uuid4),
        ),
    ]
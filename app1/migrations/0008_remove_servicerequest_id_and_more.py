# Generated by Django 4.2.4 on 2023-08-17 10:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_servicerequest_tracking_no_trackstatus_tracking_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='id',
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='tracking_no',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]

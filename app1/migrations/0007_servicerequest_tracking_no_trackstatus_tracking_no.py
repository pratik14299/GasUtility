# Generated by Django 4.2.4 on 2023-08-17 10:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_trackstatus_servicerequest_resolved_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='tracking_no',
            field=models.UUIDField(default=1, unique=True, verbose_name=uuid.uuid4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trackstatus',
            name='tracking_no',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.servicerequest'),
            preserve_default=False,
        ),
    ]

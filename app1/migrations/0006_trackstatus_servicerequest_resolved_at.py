# Generated by Django 4.2.4 on 2023-08-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_servicerequest_resolved_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='resolved_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-22 18:26

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_code',
            field=models.UUIDField(default=uuid.UUID('b6417b3a-6a4f-4581-aaff-011609b69571'), unique=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='path',
            field=models.CharField(max_length=255),
        ),
    ]

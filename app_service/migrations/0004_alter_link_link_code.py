# Generated by Django 4.1.7 on 2023-03-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_service', '0003_alter_link_link_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_code',
            field=models.UUIDField(unique=True),
        ),
    ]

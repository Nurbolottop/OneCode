# Generated by Django 5.0.1 on 2024-01-18 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_alter_service_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='image',
        ),
    ]

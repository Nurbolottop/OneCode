# Generated by Django 5.0.1 on 2024-01-17 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0019_remove_partners_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='conclution',
        ),
        migrations.RemoveField(
            model_name='news',
            name='threats',
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-17 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0020_remove_news_conclution_remove_news_threats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='threats_descriptions',
        ),
    ]

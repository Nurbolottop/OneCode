# Generated by Django 5.0.1 on 2024-01-10 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='title',
        ),
        migrations.AlterField(
            model_name='about',
            name='descriptions',
            field=models.TextField(verbose_name='Текст о нас'),
        ),
    ]
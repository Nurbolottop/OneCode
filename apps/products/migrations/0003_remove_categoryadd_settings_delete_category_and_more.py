# Generated by Django 5.0.1 on 2024-01-10 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryadd',
            name='settings',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='CategoryAdd',
        ),
    ]

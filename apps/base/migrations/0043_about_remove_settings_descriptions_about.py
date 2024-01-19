# Generated by Django 5.0.1 on 2024-01-18 10:28

import ckeditor.fields
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptions_about', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст о нас')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='image_about/', verbose_name='Фотография')),
            ],
        ),
        migrations.RemoveField(
            model_name='settings',
            name='descriptions_about',
        ),
    ]

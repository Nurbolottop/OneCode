# Generated by Django 5.0.1 on 2024-01-16 04:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_video_alter_why_why_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='descriptions_about',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Информационный текст о нас'),
        ),
    ]

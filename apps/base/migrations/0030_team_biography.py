# Generated by Django 5.0.1 on 2024-01-11 09:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_rename_experiences_team_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='biography',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='биография'),
            preserve_default=False,
        ),
    ]

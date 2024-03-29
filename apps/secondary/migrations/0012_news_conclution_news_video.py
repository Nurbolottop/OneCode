# Generated by Django 5.0.1 on 2024-01-10 09:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0011_news_letter_news_news_descriptions_news_threats_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='conclution',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='4) Описнаие Заключение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.URLField(default=1, verbose_name='Видео URL'),
            preserve_default=False,
        ),
    ]

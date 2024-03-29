# Generated by Django 5.0.1 on 2024-01-11 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_alter_team_facebook_alter_team_instagram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AddField(
            model_name='team',
            name='experiences',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='team',
            name='language',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Языки которые знает'),
        ),
        migrations.AddField(
            model_name='team',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефонный номер'),
        ),
    ]

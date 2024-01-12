# Generated by Django 5.0.1 on 2024-01-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_servicecontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('phone', models.CharField(max_length=255, verbose_name='номер телефона')),
                ('data', models.DateField(verbose_name='дата')),
                ('message', models.TextField(verbose_name='Cообщение')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]

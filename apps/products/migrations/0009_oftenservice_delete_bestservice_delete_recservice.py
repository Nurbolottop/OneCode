# Generated by Django 5.0.1 on 2024-01-11 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_bestservice_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='OftenService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='often_service')),
                ('descriptions', models.TextField(verbose_name='описание')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='often_dervice', to='products.service')),
            ],
            options={
                'verbose_name': 'Чатстый вопрос',
                'verbose_name_plural': 'Чатстые вопросы',
                'unique_together': {('service', 'title', 'image', 'descriptions')},
            },
        ),
        migrations.DeleteModel(
            name='BestService',
        ),
        migrations.DeleteModel(
            name='RecService',
        ),
    ]

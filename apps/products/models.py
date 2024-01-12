from django.db import models

from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.

class Service(models.Model):
    image = models.ImageField(
        upload_to='service',
        verbose_name='Фото'
    )
    image2 = models.ImageField(
        upload_to='service/',
        verbose_name='Фото на дитальный просмотр'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    descriptions = models.TextField(
        verbose_name='Описание заголовка'
    )
    descriptions2 = RichTextField(
        verbose_name='Описание 2'
    )
    video = models.URLField(
        verbose_name='Видео'
    )
    def __str__(self):
        return f'{self.title} - {self.descriptions}'
    class Meta():
        verbose_name='1) Услуги'
        verbose_name_plural = '1) Услуги'
  
class OftenService(models.Model):
    service = models.ForeignKey(Service, related_name='often_dervice',   on_delete=models.CASCADE)
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    image = models.ImageField(
        upload_to='often_service'
    )
    descriptions = models.TextField(
        verbose_name = 'описание'
    )
    class Meta:
        unique_together = ('service', 'title', 'image', 'descriptions')
        verbose_name = "Частый вопрос"
        verbose_name_plural = "Частые вопросы"
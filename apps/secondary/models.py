from django.db import models
from django_resized.forms import ResizedImageField 
from ckeditor.fields import RichTextField

################################################################################################################################################################################

# Create your models here.

################################################################################################################################################################################
class Slide(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image_slide/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class News(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='image_news/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Заголовок'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank = True, null = True
    )
    news_descriptions = RichTextField(
        verbose_name = '1) Описнаие новости'
    )
    letter = RichTextField(
        verbose_name = '2) Описание комментария'
    )
    threats = RichTextField(
        verbose_name = '3) Описание киберугроз'
    )
    video = models.URLField(
        verbose_name = 'Видео URL'
    )
    threats_descriptions =RichTextField(
        verbose_name = '4) Описание threats'
    )
    conclution = RichTextField(
        verbose_name = '4) Описнаие Заключение'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Function(models.Model):
    name1 = models.CharField(
        max_length = 255,
        verbose_name = 'Название1'
    )
    descriptions1 = models.TextField(
        verbose_name = 'Описание1'
    )
    name2 = models.CharField(
        max_length = 255,
        verbose_name = 'Название2'
    )
    descriptions2 = models.TextField(
        verbose_name = 'Описание2'
    )
    name3 = models.CharField(
        max_length = 255,
        verbose_name = 'Название3'
    )
    descriptions3 = models.TextField(
        verbose_name = 'Описание3'
    )
    name4 = models.CharField(
        max_length = 255,
        verbose_name = 'Название4'
    )
    descriptions4 = models.TextField(
        verbose_name = 'Описание4'
    )

    def __str__(self):
        return self.name1
    
    class Meta:
        verbose_name = 'Удобная Функция'
        verbose_name_plural = 'Удобные Функции'


    


from django.db import models

from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField 

# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    descriptions = models.TextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    descriptions_about = RichTextField(
        verbose_name="Информационный текст о нас",
        blank=True,null=True
    )
    logo = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип Компании",
        blank = True, null = True
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
    )
    whatsapp = models.URLField(
        verbose_name='Whatspp URL',
    )
    whatsapp_number = models.CharField(
        max_length = 255,
        verbose_name = "Whatsapp номер",
    )
    instagram = models.URLField(
        verbose_name='Instagram URL',
    )
    youtube = models.URLField(
        verbose_name='Youtube URL',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook URL',
        blank=True, null=True
    )
    def __str__(self):
        return self.title
    
    class Meta:
            verbose_name = "1) Основная настройка"
            verbose_name_plural = "1) Основные настройки"


class SettingsPhone(models.Model):
    settings = models.ForeignKey(Settings, related_name='phone_title', on_delete=models.CASCADE)
    phone = models.CharField(
          max_length = 255,
          verbose_name = "Телефонный номер"
     )
    class Meta:
        unique_together = ('settings', 'phone')
        verbose_name = "Дополнительный телефонный номер"
        verbose_name_plural = "Дополнительный телефонный номер"

class Service(models.Model):
    title =  models.CharField(max_length=255, verbose_name="Заголовок")
    descriptions = models.TextField(verbose_name="Описание")
    image = ResizedImageField(verbose_name='Фотография', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "2) Наша услуга"
        verbose_name_plural = "2) Наши услуги"

class ChooseUs(models.Model):
    title =  models.CharField(max_length=50, verbose_name="Заголовок")
    descriptions = models.TextField(verbose_name="Описание")
    why_1 = models.CharField(max_length=100, verbose_name="Почему_1")
    why_2 = models.CharField(max_length=100, verbose_name="Почему_2")
    why_3 = models.CharField(max_length=100, verbose_name="Почему_3")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "3) Почему мы"
        verbose_name_plural = "3) Почему мы"

class Team(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='team_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    work = models.CharField(
        max_length = 255,
        verbose_name = 'Должность'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    facebook = models.URLField(
        verbose_name = 'facebook URL'
    )
    twitter = models.URLField(
        verbose_name = 'twitter URL'
    )
    instagram = models.URLField(
        verbose_name = 'instagram URL'
    )
    youtube = models.URLField(
        verbose_name = 'youtube URL'
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = 'Телефонный номер',
        blank=True, null= True
    )
    email = models.EmailField(
        verbose_name = 'Почта',
        blank=True, null= True
    )
    language = models.CharField(
        max_length = 255,
        verbose_name = 'Языки которые знает',
        blank=True, null= True
    )
    experience = models.CharField(
        max_length = 255,
        verbose_name = 'Опыт работы',
        blank=True, null= True
    )
    biography = RichTextField(
        verbose_name = 'биография'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '4) Команда'
        verbose_name_plural = '4) Команды'

class Review(models.Model):
    description = RichTextField(
        verbose_name = 'Сам отзыв'
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='review_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '5) Отзыв'
        verbose_name_plural = '5) Отзывы'


    
class Video(models.Model):
    Video_url = models.URLField(
        verbose_name = 'Видео URL'
    )

    class Meta:
        verbose_name = '6) Видео'
        verbose_name_plural = '6) Видео'


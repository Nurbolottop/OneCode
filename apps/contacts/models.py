from django.db import models
from django.core.mail import EmailMessage
from ckeditor.fields import RichTextField

# Create your models here.
class BlogContact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(
        verbose_name = 'Cообщение'
    )
    def __str__(self):
        return self.name
    class Meta():
        verbose_name='Зопрос на Блоге'
        verbose_name_plural='Зопросs на Блоге'
        
class ServiceContact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(
        verbose_name = 'Cообщение'
    )
    def __str__(self):
        return self.name
    class Meta():
        verbose_name='Зопрос о услуге'
        verbose_name_plural='Зопросы на услуги'
################################################################################################################################################################################

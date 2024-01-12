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
        
class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='имя'
    )
    email = models.EmailField(
        verbose_name='почта'
    )
    country = models.CharField(
        max_length=255,
        verbose_name='страна'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='номер телефона'
    )
    data = models.DateField(
        verbose_name='дата'
    )
    message = models.TextField(
        verbose_name='Cообщение'
    )
    
    def __str__(self):
        return f'{self.name} = {self.mesage}'
    class Meta:
        verbose_name='Контакт'
        verbose_name_plural='Контакты'
        
################################################################################################################################################################################

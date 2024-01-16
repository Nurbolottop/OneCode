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
        verbose_name='1) Запрос на Блоге'
        verbose_name_plural='1) Запросы на Блоге'
        
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
        verbose_name='2) Запрос о услуге'
        verbose_name_plural='3) Запросы на услуги'
        
        
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
        return f'{self.name} = {self.message}'
    
    class Meta:
        verbose_name='4) Контакт'
        verbose_name_plural='4) Контакты'

class Subscriber(models.Model):
    email = models.EmailField(
        verbose_name = "Почта пользователя"
    )
    subscribed_at = models.DateTimeField(auto_now_add=True,verbose_name = "Дата подписки") 
    def __str__(self):
        return f"{self.email} - {self.subscribed_at}"
    
    class Meta:
        verbose_name = "3) Пользователи для рассылки"
        verbose_name_plural = "3) Пользователи для рассылки"
        
################################################################################################################################################################################

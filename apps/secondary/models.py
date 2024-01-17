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
        verbose_name = '1) Слайд'
        verbose_name_plural = '1) Слайды'


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
    video = models.URLField(
        verbose_name = 'Видео URL'
    )
   
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2) Новость'
        verbose_name_plural = '2) Новости'


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
        verbose_name = '3) Удобная Функция'
        verbose_name_plural = '3) Удобные Функции'


    


#  пока не надо деди
# class GoodPrice(models.Model):
#     title = models.CharField(
#         max_length = 255,
#         verbose_name = 'Название'
#     )
#     descriptions = models.CharField(
#         max_length = 255,
#         verbose_name = 'Описание'
#     )
#     price = models.CharField(
#         max_length = 255,
#         verbose_name = 'Цена'
#     )
    
#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = '5) Лучшая цена'
#         verbose_name_plural = '5) Лучшие цены'

# class GoodPriceFeatcher(models.Model):
#     place_info = models.ForeignKey(GoodPrice,related_name = "price_inline_info", on_delete  = models.CASCADE )
#     title = models.CharField(
#         max_length = 255,
#         verbose_name = 'Характиристика'
#     )

#     class Meta:
#         unique_together = ('place_info', 'title')


class Partners(models.Model):
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='partner_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    class Meta:
        verbose_name = '5) Партнер'
        verbose_name_plural = '5) Партнеры'


class Question(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя' 
    ) 
    email = models.EmailField(
        verbose_name = 'Почта'
    )
    comment = models.TextField(
        verbose_name = 'Комментарий'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Faq(models.Model):
    comments = models.ManyToManyField(Question, related_name='faq_comments', verbose_name='Комментарии к FAQ')

    def __str__(self):
        return f"FAQ #{self.pk}"

    class Meta:
        verbose_name = '4) Частый вопрос'
        verbose_name_plural = '4) Частые вопросы'
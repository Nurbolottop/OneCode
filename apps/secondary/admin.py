from django.contrib import admin

from apps.secondary import models

# Register your models here.

################################################################################################################################################################################
class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

class NewsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', )
    search_fields = ('title', )

class FunctionFilterAdmin(admin.ModelAdmin):
    list_filter = ('name1', )
    list_display = ('name1', )
    search_fields = ('name1', )

class FaqFilterAdmin(admin.ModelAdmin):
    list_filter = ('question', )
    list_display = ('question','answer' )
    search_fields = ('question', 'answer')




admin.site.register(models.Partners)
admin.site.register(models.Faq, FaqFilterAdmin)
admin.site.register(models.Function, FunctionFilterAdmin)
admin.site.register(models.News, NewsFilterAdmin)
admin.site.register(models.Slide, SlideFilterAdmin)





# class GoodPriceInline(admin.TabularInline):
#     model = models.GoodPriceFeatcher
#     extra = 1

# class GoodPriceFilterAdmin(admin.ModelAdmin):
#     list_filter = ('title', )
#     list_display = ('title', )
#     search_fields = ('title', )
#     inlines = [GoodPriceInline]


# admin.site.register(models.GoodPrice, GoodPriceFilterAdmin)
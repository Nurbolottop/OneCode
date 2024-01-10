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


admin.site.register(models.Function, FunctionFilterAdmin)
admin.site.register(models.News, NewsFilterAdmin)
admin.site.register(models.Slide, SlideFilterAdmin)


from django.contrib import admin
from django.contrib.auth.models import User,Group

################################################################################################################################################################################

from apps.base import models 
from apps.base.models import Service, ChooseUs

# Register your models here.
class SettingsPhoneInline(admin.TabularInline):
    model = models.SettingsPhone
    extra = 1  


class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [SettingsPhoneInline]

class TeamFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')

    
class ReviewFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

################################################################################################################################################################################


admin.site.register(models.About)
admin.site.register(models.Video)
admin.site.register(models.Review)
admin.site.register(models.Team, TeamFilterAdmin)
admin.site.register(models.Settings, SettingsFilterAdmin)
admin.site.register(Service)
admin.site.register(ChooseUs)
################################################################################################################################################################################

admin.site.unregister(User)
admin.site.unregister(Group)

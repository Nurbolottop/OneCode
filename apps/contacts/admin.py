from django.contrib import admin

################################################################################################################################################################################
from apps.contacts import models 

# Register your models here.
admin.site.register(models.Subscriber)
admin.site.register(models.BlogContact)
admin.site.register(models.ServiceContact)
admin.site.register(models.Contact)
################################################################################################################################################################################

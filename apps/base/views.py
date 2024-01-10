from django.shortcuts import render,redirect

################################################################################################################################################################################

from apps.base import models 
from apps.telegram_bot.views import get_text

# Create your views here.
def index(request):
#Base----------------------------------------------------------
    settings = models.Settings.objects.latest("id")
    service = models.Service.objects.all()

#Secondary----------------------------------------------------------

#Contacts ----------------------------------------------------------
    
    return render(request,'base/index.html', locals())

################################################################################################################################################################################

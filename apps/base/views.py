from django.shortcuts import render,redirect

################################################################################################################################################################################

from apps.base.models import Settings, Team
from apps.secondary import models
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
#Base----------------------------------------------------------
    settings = Settings.objects.latest("id")
    return render(request,'base/index.html', locals())

def team(request):
    team = Team.objects.all()
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    return render(request, 'base/team.html', locals())
#Secondary----------------------------------------------------------
def blog(request):
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    all_news = models.News.objects.all()
    
    items_per_page = 6
    
    paginator = Paginator(all_news, items_per_page)
    
    page = request.GET.get('page')
    
    try:
        news_page = paginator.page(page)
    except PageNotAnInteger:
        news_page = paginator.page(1)
    except EmptyPage:
        news_page = paginator.page(paginator.num_pages)


    context = {
        'settings': settings,
        'slide': slide,
        'news_page': news_page,
    }

    return render(request, 'secondary/blog.html', locals())
    
def blog_detail(request, id):
    news_blog = models.News.objects.get(id=id)
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    all_news = models.News.objects.all()

    last_news_count = 4

    last_news = all_news.order_by('-created_at')[:last_news_count]

    context = {
        'settings': settings,
        'slide': slide,
        'last_news': last_news,
    }


    return render(request, 'secondary/blog_detail.html', locals())

def faq(request):
    faq = models.Faq.objects.all()
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    function =  models.Function.objects.latest('id')
    return render(request, 'secondary/faq.html', locals())


def price(request):
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    function =  models.Function.objects.latest('id')
    partners = models.Partners.objects.all()
    # goodprice = models.GoodPrice.objects.latest('id')
    # price = models.GoodPrice.objects.all()

    return render(request, 'secondary/price.html', locals())


def team_details(request, id):
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    function =  models.Function.objects.latest('id')
    details =Team.objects.get(id=id)
    return render(request, 'secondary/team-details.html', locals())


#Contacts ----------------------------------------------------------
    
    

################################################################################################################################################################################

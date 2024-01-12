from django.shortcuts import render,redirect

################################################################################################################################################################################

from apps.base.models import Settings, Team
from apps.secondary import models
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.contacts.models import BlogContact,ServiceContact, Contact
from apps.products.models import Service
\
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

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if BlogContact.objects.filter(message=message).exists():
            return render(request, 'secondary/blog_detail.html', {'error_message': 'Такое сообщение уже отправлено'})
        
        contact = BlogContact.objects.create(name=name, email=email, message=message)
        
        get_text(f"""
Оставили запрос о блоге
👇👇👇👇👇👇👇👇👇👇👇
Имя: {name}.
Почта: {email}.
Сообщение: {message}."""
        )
    return render(request, 'secondary/blog_detail.html', locals())

def faq(request):
    faq = models.Faq.objects.all()
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    function =  models.Function.objects.latest('id')
    return render(request, 'secondary/faq.html', locals())
def service(request):
    settings = Settings.objects.latest("id")
    services = Service.objects.all()
    return render(request, 'service/service-1.html', locals())

def service_detail(request, id):
    service = Service.objects.get(id=id)    
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    all_news = models.News.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if ServiceContact.objects.filter(message=message).exists():
            return render(request, 'service/service-details.html', {'error_message': 'Такое сообщение уже отправлено'})
        
        contact = BlogContact.objects.create(name=name, email=email, message=message)
        
        get_text(f"""
Оставили запрос о услуге
👇👇👇👇👇👇👇👇👇👇👇
Имя: {name}.
Почта: {email}.
Сообщение: {message}."""
        )
    return render(request, 'service/service-details.html',locals())



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

def contact(request):
    settings = Settings.objects.latest("id")
    
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        data = request.POST.get('data')
        message = request.POST.get('message')
        existing_contact = Contact.objects.filter(message=message).first()

        if not existing_contact:
            contact = Contact.objects.create(name=name, email=email, phone=phone, country=country, data=data, message=message)
        
            get_text(f"""
Отправлен запрос о обратной связи 
👇👇👇👇👇👇👇👇👇👇👇
Имя: {name}.
Email: {email}.
Номер телефона: {phone}.
Страна: {country}.
Дата: {data}.
Сообщение: {message}.
""")
    return render(request, 'base/contact.html', locals())
################################################################################################################################################################################

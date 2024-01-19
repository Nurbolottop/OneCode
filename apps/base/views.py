from django.shortcuts import render,redirect

################################################################################################################################################################################

from apps.base.models import Settings, Team, Review, Service, ChooseUs, About, Video
from apps.secondary import models
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from apps.contacts.models import BlogContact,ServiceContact, Contact, Subscriber
# from apps.products.models import Service

# Create your views here.
def index(request):
#Base----------------------------------------------------------
    title = "Главная "
    about = About.objects.latest('id')
    settings = Settings.objects.latest("id")
    reviews = Review.objects.all()
    service = Service.objects.all()
    partners = models.Partners.objects.all()  
    choose_us = ChooseUs.objects.latest('id')  

   
    
    return render(request,'base/index.html', locals())

def team(request):
    title = "Команда"
    team = Team.objects.all()
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')

    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            existing_subscriber = Subscriber.objects.filter(email=email).first()

            if not existing_subscriber:
                subscribe = Subscriber.objects.create(email=email)
                get_text(f"""
                    ✅ Пользователь подписался на рассылку
                            
    ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                            
    Почта пользователя: {email} 
    """)

    return render(request, 'base/team.html', locals())

def about(request):
    team = Team.objects.all()
    video = Video.objects.latest('id')
    about = About.objects.latest('id')
    choose_us = ChooseUs.objects.latest('id') 
    partners = models.Partners.objects.all()
    title = "О нас"

    function =  models.Function.objects.latest('id')

    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')

    if request.method == 'POST':
            if "newslater" in request.POST:
                email = request.POST.get('email') 
                existing_subscriber = Subscriber.objects.filter(email=email).first()

                if not existing_subscriber:
                    subscribe = Subscriber.objects.create(email=email)
                    get_text(f"""
                        ✅ Пользователь подписался на рассылку
                                
        ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                                
        Почта пользователя: {email} 
        """)
            
    return render(request, 'base/about.html', locals())

    
#Secondary----------------------------------------------------------
def blog(request):
    title = "Новости"
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
    if request.method == 'POST':
            if "newslater" in request.POST:
                email = request.POST.get('email') 
                existing_subscriber = Subscriber.objects.filter(email=email).first()

                if not existing_subscriber:
                    subscribe = Subscriber.objects.create(email=email)
                    get_text(f"""
                        ✅ Пользователь подписался на рассылку
                                
        ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                                
        Почта пользователя: {email} 
        """)

    return render(request, 'secondary/blog.html', locals())
    

    return render(request, 'secondary/blog.html', locals())
    
def blog_detail(request, id):
    title = "Новости подробнее"
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
    title = "Частые вопросы"
    faq = models.Faq.objects.first()  # Assuming you have only one FAQ instance
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    function = models.Function.objects.latest('id')

    if request.method == 'POST':
        if 'faq_form' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            user_comment = request.POST.get('message')

            existing_question = models.Question.objects.filter(name=name, email=email).first()
            if existing_question:
                # Update the existing question
                existing_question.comment = user_comment
                existing_question.save()
                faq.comments.add(existing_question)
            else:
                new_comment = models.Question(name=name, email=email, comment=user_comment)
                new_comment.save()

                faq.comments.add(new_comment)

            if request.method == 'POST':
                if "newslater" in request.POST:
                    email = request.POST.get('email') 
                    existing_subscriber = Subscriber.objects.filter(email=email).first()

                    if not existing_subscriber:
                        subscribe = Subscriber.objects.create(email=email)
                        get_text(f"""
                            ✅ Пользователь подписался на рассылку
                                    
            ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                                    
            Почта пользователя: {email} 
            """)

    
            
    return render(request, 'secondary/faq.html', locals())

def service(request):
    title = "Услуги"
    services = Service.objects.all() 
    settings = Settings.objects.latest("id")

    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            existing_subscriber = Subscriber.objects.filter(email=email).first()

        if request.method == 'POST':
            if "newslater" in request.POST:
                    email = request.POST.get('email') 
                    existing_subscriber = Subscriber.objects.filter(email=email).first()

                    if not existing_subscriber:
                        subscribe = Subscriber.objects.create(email=email)
                        get_text(f"""
                            ✅ Пользователь подписался на рассылку
                                    
            ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                                    
            Почта пользователя: {email} 
            """)

    return render(request, 'service/service-1.html', locals())


def service_detail(request, id):
    title = "Услуги побробнее"
    services = Service.objects.get(id=id) 
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
    title = "Цены"
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    function =  models.Function.objects.latest('id')
    partners = models.Partners.objects.all()
    # goodprice = models.GoodPrice.objects.latest('id')
    # price = models.GoodPrice.objects.all()

    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            existing_subscriber = Subscriber.objects.filter(email=email).first()

            if not existing_subscriber:
                subscribe = Subscriber.objects.create(email=email)
                get_text(f"""
                    ✅ Пользователь подписался на рассылку
                            
    ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                            
    Почта пользователя: {email} 
    """)
            
    return render(request, 'secondary/price.html', locals())


def team_details(request, id):
    title = "Команды"
    settings = Settings.objects.latest("id")
    slide = models.Slide.objects.latest('id')
    function =  models.Function.objects.latest('id')
    details =Team.objects.get(id=id)

    if request.method == 'POST':
        if "newslater" in request.POST:
            email = request.POST.get('email') 
            existing_subscriber = Subscriber.objects.filter(email=email).first()

            if not existing_subscriber:
                subscribe = Subscriber.objects.create(email=email)
                get_text(f"""
                    ✅ Пользователь подписался на рассылку
                            
    ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                            
    Почта пользователя: {email} 
    """)
    return render(request, 'secondary/team-details.html', locals())


#Contacts ----------------------------------------------------------

def contact(request):
    title = "Контакты"
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

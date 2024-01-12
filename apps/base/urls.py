from django.urls import path  
from apps.base import views


################################################################################################################################################################################

urlpatterns = [
    path("", views.index, name="index"),
    # path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog' ),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('faq/', views.faq, name='faq'),
    path('service_detail/<int:id>/', views.service_detail, name='service_detail'),
    path("service/", views.service, name="service"),
    path('price', views.price, name='price'),
    path('team_details/<int:id>/', views.team_details, name='team_details'),
    path('contact/', views.contact, name='contact'),
<<<<<<< HEAD
    # path('login/', views.login, name='login')
=======
    path('login/', views.login, name='login')
>>>>>>> 2403084e14633485b35442b6d22ba7ef32bc8b2a

]
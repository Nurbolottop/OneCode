from django.urls import path  
from apps.base import views


################################################################################################################################################################################

urlpatterns = [
    path("", views.index, name="index"),
    path('blog/', views.blog, name='blog' ),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('faq/', views.faq, name='faq'),
    path('service_detail/<int:id>/', views.service_detail, name='service_detail'),
    path("service/", views.service, name="service"),

]
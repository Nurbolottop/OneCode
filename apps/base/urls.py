from django.urls import path  
from apps.base import views


################################################################################################################################################################################

urlpatterns = [
    path("", views.index, name="index"),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog' ),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('faq/', views.faq, name='faq'),
    path('price/', views.price, name='price'),
    path('team_details/<int:id>/', views.team_details, name='team_details'),
    
]
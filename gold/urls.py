from django.urls import path
from . import views


urlpatterns =[
    path('', views.index,name='index'),
    path('service/', views.service,name="service"),
    path('contacts/', views.contacts,name="contact"),
    path('about/', views.about,name="about"),
    path('sign_up/', views.sign_up,name="sign_up"),
    path('sign_in/', views.sign_in,name="sign_in"),
    path('admini/', views.admin,name="admin"),
    path('cart/', views.cart,name="cart"),
    path('delete/',  views.delete,name="delete"),
    path('newsletter/', views.news_letter,name="news_letter"),
    path('Add_Item_to_cart/', views.Add_Item_to_cart,name="Add_Item_to_cart"),
    
]

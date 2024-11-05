from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.index,name='index'),
    path('service/', views.service,name="service"),
    path('contacts/', views.contacts,name="contact"),
    path('about/', views.about,name="about"),
    path('sign_up/', views.sign_up,name="sign_up"),
    path('sign_in/', views.sign_in,name="sign_in"),
    path('log_out/', views.log_out,name="log_out"),
    path('/', views.userpage,name="userpage"),
    path('admini/', views.admin,name="admin"),
    path('delete/', views.delete,name="delete"),
    path('delete_from_cart/', views.delete_from_cart,name="delete_from_cart"),
    path('cart/', views.cart,name="cart"),
    path('increase_quantity/', views.increase,name="increase_quantity"),
    path('decrease_quantity/', views.decrease,name="decrease_quantity"),
    path('newsletter/', views.news_letter,name="news_letter"),
    path('Add_Item_to_cart/', views.Add_Item_to_cart,name="Add_Item_to_cart"),
    path('payments/', views.payments,name="payments"),
    
]
if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

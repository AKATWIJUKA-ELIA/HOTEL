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
    path('home/', views.userpage,name="userpage"),
    path('admini/', views.admin,name="admin"),
    path('admin-login/', views.admin_login,name="admin-login"),
    path('admin-signup/', views.admin_signup,name="admin_signup"),
    path('delete/', views.delete,name="delete"),# Deleting Products
    path('update/', views.update,name="update"), # updating products
    path('delete_from_cart/', views.delete_from_cart,name="delete_from_cart"),
    path('cart/', views.cart,name="cart"),
    path('increase_quantity/', views.increase,name="increase_quantity"),
    path('decrease_quantity/', views.decrease,name="decrease_quantity"),
    path('newsletter/', views.news_letter,name="news_letter"),
    path('Add_Item_to_cart/', views.Add_Item_to_cart,name="Add_Item_to_cart"),
    path('payments/', views.payments,name="payments"),
    path('Send_email/', views.Send_email,name="Send_email"),
    
]
if settings.DEBUG:
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.shortcuts import render, redirect,get_object_or_404
from gold.models import News_letter, Customers,Products,Orders,Cart
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.http import JsonResponse



# class Cart():
#     def __init__(self, request):
#         self.session = request.session
#         # Get the current session key if it exists
#         cart = self.session.get('session_key')
#         # If the user is new, no session key! Create one!
#         if 'session_key' not in request.session:
#             cart = self.session['session_key'] = {}
#         # Make sure cart is available on all pages of site
#         self.cart = cart
#     def add(self, product):
#           pass
          
def index(request):
      
      data = serializers.serialize("python",Products.objects.all() )
      print(data)
      items_on_cart = Cart.objects.count()
      context = {'data':data,
                 'items_on_cart':items_on_cart,
                 } 
      
      print(items_on_cart)
     
      
      return  render(request, 'index.html',context=context)

def admin(request):
      data = serializers.serialize("python",Products.objects.all() )   
      context = {'data':data,}
      if request.method == 'POST':
            product_name = request.POST['product_name']
            price = request.POST['price']
            product_description  = request.POST['product_description']
            product_image = request.FILES.get('image')
            
            # print(request.FILES)
            print(product_image)
            
            new_product = Products.objects.create(product_name=product_name,product_price=price,product_description=product_description,product_image=product_image)
            new_product.save() 
      return render(request, 'admin.html',context=context)

def delete(request):
      if request.method == 'POST':
            product_id = request.POST['product_id']
            product = Products.objects.get(product_id=product_id)
            product.delete()
            messages.info(request,  'Product deleted successfully')

      return render(request, 'delete.html')


def service(request):
    return render(request, 'service.html')

def contacts(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def cart(request):
      # cart_item = serializers.serialize("python",Cart.objects.all() )
      cart_item =  Cart.objects.all()
      # print(sample)
      # cart_ids =   []
      # for item in sample:
      #       cart_item = Cart.objects.get(pk=item.Cart_id_id)
            # cart_ids.append(item.Cart_id_id)
      # print(cart_ids)
      # for cart_id in cart_ids:
      #       cart_item = Cart.objects.get(pk=cart_id)
     
      # print(cart_item.Cart_id.product_name)
      
      items_on_cart = Cart.objects.count()
      context = {'items_on_cart':items_on_cart,
                 'cart_item':cart_item,
                 }
      return render(request, 'cart.html', context=context)

def Add_Item_to_cart(request):
      if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            print(product_id)
            product = Products.objects.get(product_id=product_id)
            print(product)
            if Cart.objects.filter(Cart_id=product_id).exists():
                  messages.error(request, 'product already added to cart, check your cart to increase the quantity')
                  return render(request, 'index.html')
            else:
                  newcart = Cart.objects.create(Cart_id=product,
                                                # Cart_image=product.product_image,Cart_name=product.product_name,Cart_price=product.product_price,Cart_description=product.product_description
                                                )
                  
                  newcart.save()
                  print(newcart)
                  messages.success(request, 'Product Successfully added to cart')
                  return render(request, 'index.html')
             
      return render(request, 'index.html')


# =========S I G N I N G    U P=========== #
def sign_up(request):
      if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            password2 = request.POST.get('password2')
            
            if password == password2:
                  # user_password = set_password(password2)
                  
                  if Customers.objects.filter(username = username).exists():
                        messages.error(request,"Username already exists.")
                        return render(request, 'sign_up.html')
                  
                  elif Customers.objects.filter(email = email).exists():
                        messages.error(request,"email already exists.")
                        return render(request, 'sign_up.html')   
                  else:
                        NewUser = Customers.objects.create(username=username,email=email,password=password2,phone_number=phone,address='')
                        NewUser.set_password(password2)
                        NewUser.save()
                        messages.success(request, "Your account has been successfully created you will be redirected to the login page")
                        return redirect('index') 
            
            else:
                  messages.error(request,"Passwords do not match.")
                  return render(request, 'sign_up.html')
      return render(request, 'sign_up.html')

def sign_in(request):
      if request.method == "POST":
            username = request.POST.get('username')#.lower()
            password = request.POST.get('password')
            print(username + password)
            
            user = authenticate(username = username, password=password)
            
            if user is not None:                        
                  login(request,user)
                  username=user.username
                  #self.logged_in = True
                  return render(request,'userpage.html', {'username': username.capitalize()})
                  
            else:
                  messages.error(request, "bad credentials")
                  return redirect('sign_in')
            #retrieving data
      data = serializers.serialize("python",Customers.objects.all() )
      context = {'data':data,}    
                  
      return render(request, "sign_in.html", context)

def news_letter(request):
    
    if request.method == "POST":
        email = request.POST["email"]
        print(email)
        
    if News_letter.objects.filter(email=email).exists():
        messages.info(request,"email already exists")
    else:
        new = News_letter.objects.create(email=email)
        new.save()
        messages.info(request, "Thank you for Subscribing")
    return render(request, 'index.html')
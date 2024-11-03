from django.shortcuts import render, redirect,get_object_or_404
from gold.models import News_letter, Customers,Products,Orders,Cart
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Sum



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
      if request.user.is_authenticated:
            return redirect('userpage')
      else:
            data = serializers.serialize("python",Products.objects.all() )
            print(data)
            # items_on_cart = Cart.objects.count()
            context = {'data':data,
                  #      'items_on_cart':items_on_cart,
                  } 
            
            
            # print(items_on_cart)
            return  render(request, 'index.html',context=context)

def userpage(request):
      if request.user.is_authenticated:
            try:
                  data = serializers.serialize("python",Products.objects.all() )
                  # data = Products.objects.all() 
                  items_on_cart =  Cart.objects.all().filter(cart_user_id=request.user.Customer_id)
            except Cart.DoesNotExist:
                  context = {'data':data,
                        'username':request.user.username
                        }
                  return  render(request, 'userpage.html',context)
            finally:
                  # items_on_cart = Cart.objects.count()
                  context = {'data':data,
                             'items_on_cart':items_on_cart.count(),
                              'username':request.user.username
                              }
                   
                   
      # print(items_on_cart)
      return  render(request, 'userpage.html',context=context)

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
      if request.user.is_authenticated:
            try:
                  # cart_item = serializers.serialize("python",Cart.objects.all() )
                  cart_item =  Cart.objects.all().filter(cart_user_id=request.user.Customer_id)
                  
                  print(cart_item)
            except Cart.DoesNotExist:
                  messages.info(request, 'your cart is empty')
                  return render(request, 'cart.html', )
                        
            # items to sum up
            def get_total_cart_amount():
                  total_amount = Cart.objects.filter(cart_user_id=request.user.Customer_id).aggregate(total=Sum('Cart_amount'))['total']
                  return total_amount or 0
            # print(get_total_cart_amount(request.user.Customer_id))
            total_sum =  get_total_cart_amount()
            print(total_sum)
            
            
            items_on_cart = Cart.objects.all().filter(cart_user_id=request.user.Customer_id).count()
            context = {'items_on_cart':items_on_cart,
                  'cart_item':cart_item,
                  'total':total_sum,
                  }
      return render(request, 'cart.html', context=context)
###==========================================######
#           A D D I N G   I T E M   TO  C A R T
#============================================######
def Add_Item_to_cart(request):
    if request.user.is_authenticated:
        name = request.user
        customer = Customers.objects.get(username=name)
        
        if request.POST.get('action') == 'post':
            product_id = int(request.POST.get('product_id'))
            product = Products.objects.get(product_id=product_id)

            # Check if the product is already in the cart
            if Cart.objects.filter(cart_user=customer, Product_id=product_id).exists():
                messages.info(request, 'Product already added to cart, check your cart to increase the quantity')
                return render(request, 'userpage.html')
            else:
                # Create a new cart item
                newcart = Cart.objects.create(
                    cart_user=customer,
                    Product_id=product_id,
                    Cart_image=product.product_image,
                    Cart_name=product.product_name,
                    Cart_price=product.product_price,
                    Cart_description=product.product_description
                )
                newcart.save()
                messages.success(request, 'Product successfully added to cart')
                return render(request, 'index.html')
        
        return render(request, 'index.html')
    else:
        messages.error(request, 'You must have an account to be able to add to cart')
        return render(request, 'sign_in.html')
      
      
      


###==========================================######
#          I N C R E A S E   Q U A N T I T Y   ON  CART
#============================================######
def increase(request):
      if request.user.is_authenticated:
            name = request.user
            customer = Customers.objects.get(username=name)
            cart_id = request.POST['cart_id']
            print(cart_id)
      
            cart_object = Cart.objects.get(cart_user_id=customer.Customer_id, cart_id=cart_id)
            # if cart_objects.cart_user_id == customer.Customer_id and cart_objects.cart_id == cart_id:
                  # new_object = Cart.objects.get(cart_user_id=customer.Customer_id, cart_id=cart_id)
            cart_object.quantity += 1
            cart_object.Cart_amount = cart_object.Cart_price* cart_object.quantity
            cart_object.save()
            print(cart_object.quantity)
      return redirect('cart')

###==========================================######
#          D E C R E A S E   Q U A N T I T Y   ON  CART
#============================================######
def decrease(request):
      if request.user.is_authenticated:
            name = request.user
            customer = Customers.objects.get(username=name)
            cart_id = request.POST['cart_id']
            print(cart_id)
      
            cart_object = Cart.objects.get(cart_user_id=customer.Customer_id, cart_id=cart_id)
            # if cart_objects.cart_user_id == customer.Customer_id and cart_objects.cart_id == cart_id:
                  # new_object = Cart.objects.get(cart_user_id=customer.Customer_id, cart_id=cart_id)
            if cart_object.quantity > 1:
                  cart_object.quantity -= 1
                  cart_object.save()
                  print(cart_object.quantity)
            else:
                  pass
      return redirect('cart')    
      
      
###==========================================######
#          D E L E T E  I T E M  F R O M    C A R T
#============================================######
def delete_from_cart(request):
      if request.user.is_authenticated:
            name = request.user
            customer = Customers.objects.get(username=name)
            cart_id = request.POST['cart_id']
            cart_object = Cart.objects.get(cart_user_id=customer.Customer_id, cart_id=cart_id)
            cart_object.delete()
            messages.info(request,  'Product deleted successfully')
      return redirect('cart')


###==========================================######
#           S I G N I N G    U P
#============================================######
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
                  # data = serializers.serialize("python",Products.objects.all() )
                  # context = {'data':data,
                  #            'username': username.capitalize()} 
                  return redirect('userpage')
                  
            else:
                  messages.error(request, "bad credentials")
                  return redirect('sign_in')
            #retrieving data
      data = serializers.serialize("python",Customers.objects.all() )
      context = {'data':data,}    
                  
      return render(request, "sign_in.html", context)

def log_out(request):
      logout(request)
      return  redirect('index')


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
from django.shortcuts import render, redirect,get_object_or_404
from gold.models import News_letter, Customers,Products,Orders,Cart,Gallery
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Sum
from django.db import transaction
import requests
import uuid
from django.conf import settings
import smtplib
import ssl
from email.message import EmailMessage
from django.core.mail import send_mail
import base64




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
            data = serializers.serialize("python",Products.objects.filter(product_cartegory='drinks'))
            lunch = serializers.serialize("python",Products.objects.filter(product_cartegory='Lunch'))
            salad = serializers.serialize("python",Products.objects.filter(product_cartegory='salad'))
            print(data)
            # items_on_cart = Cart.objects.count()
            context = {'data':data,
                       'lunch':lunch,
                       'salad':salad,
                       'MEDIA_URL': settings.MEDIA_URL,
                  #      'items_on_cart':items_on_cart,
                  } 
            
            
            # print(items_on_cart)
            return  render(request, 'index.html',context=context)

def userpage(request):
      if request.user.is_authenticated:
            try:
                  data = serializers.serialize("python",Products.objects.filter(product_cartegory='drinks'))
                  lunch = serializers.serialize("python",Products.objects.filter(product_cartegory='Lunch'))
                  salad = serializers.serialize("python",Products.objects.filter(product_cartegory='salad'))
                  # data = Products.objects.all() 
                  items_on_cart =  Cart.objects.all().filter(cart_user_id=request.user.Customer_id)
            except Cart.DoesNotExist:
                  context = {'data':data,
                             
                        'username':request.user.username[:5]
                        }
                  return  render(request, 'userpage.html',context)
            finally:
                  # items_on_cart = Cart.objects.count()
                  context = {'data':data,
                             'lunch':lunch,
                             'salad':salad,
                             'MEDIA_URL': settings.MEDIA_URL,
                             'items_on_cart':items_on_cart.count(),
                              'username':request.user.username[:5]
                              }
            # print(items_on_cart)
            return  render(request, 'userpage.html',context=context)
      else:
            return redirect('sign_in')
def profile(request):
      if request.user.is_authenticated:
            email = request.user.email
            address = request.user.address
            phone = request.user.phone_number
            user = Customers.objects.get(Customer_id=request.user.Customer_id)
            items_on_cart = Cart.objects.all().filter(cart_user_id=request.user.Customer_id).count()
            orders = Orders.objects.filter(order_user=user)
            # print(address)
            context={
                  'email':email,
                  'address':address,
                  'phone':phone,
                  'username':request.user.username[:5],
                  'items_on_cart':items_on_cart,
                  'orders':orders,
            }

            return render(request, 'profile.html', context=context)
               
def edit_profile(request):
      if request.user.is_authenticated:
            if request.method == 'POST':
                  email = request.POST['email']
                  # print(email)
                  phone = request.POST.get('phone')
                  password = request.POST.get('password')
                  address = request.POST.get("address")
                  user = Customers.objects.get(Customer_id=request.user.Customer_id)
                  if email == None:
                        user.email = user.email
                  else:
                        user.email = email
                  if phone == None:
                        user.phone_number = user.phone_number
                  else:
                        user.phone_number = phone
                  if password == None:
                        user.password = user.password
                  else:
                        user.password = password
                  if address == None:
                        user.address = user.address
                  else:
                        user.address = address
                  user.save()
      return redirect('profile')


def admin_signup(request):
      if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            phone = request.POST['phone']
            password = request.POST['password']
            confirm_password = request.POST.get('confirm_password')
            if password == confirm_password:
                  if Customers.objects.filter(username = username).exists():
                        messages.error(request,"Username already exists.")
                        return render(request, 'administrator/signup.html')
                  
                  elif Customers.objects.filter(email = email).exists():
                        messages.error(request,"email already exists.")
                        return render(request, 'administrator/signup.html')   
                  else:
                        NewAdmin = Customers.objects.create(username=username,email=email,password=confirm_password,phone_number=phone,address="")
                        NewAdmin.is_superuser = True
                        NewAdmin.set_password(confirm_password)
                        NewAdmin.save()
                        
                        user = authenticate(username = username, password=password)
                        if user is not None:
                              login(request, user)
                              return redirect('admin') 
            
            else:
                  messages.error(request,"Passwords do not match.")
                  return render(request, 'administrator/signup.html')
      return render(request, 'administrator/signup.html')      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
def admin_login(request):  
      
      
      if request.method =='POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password=password)
            if user is not None and user.is_superuser:
                  login(request, user)
                  return redirect('admin')
            else:
                  messages.error(request,"Invalid username or password.")
                  return render(request, 'administrator/login.html')
      return render(request, 'administrator/login.html')      
            
                  
def admin(request):
      if request.user.is_authenticated:
            data = serializers.serialize("python",Products.objects.all() ) 
            
            orders = Orders.objects.all()
            available_products = Products.objects.count()
            total_orders = Orders.objects.count()
            total_customers = Customers.objects.count()
            gallery = Gallery.objects.all()
            context = {'data':data,
                       'orders':orders,
                       'gallery':gallery,
                       'username':request.user,
                  'available_products':available_products,
                  'total_customers':total_customers,
                  'total_orders':total_orders,
                  'MEDIA_URL': settings.MEDIA_URL,}
            if request.method == 'POST':
                  product_name = request.POST['product_name']
                  price = request.POST['price']
                  product_description  = request.POST['product_description']
                  product_cartegory  = request.POST['cartegory']
                  product_image = request.FILES.get('image')
                  
                  # print(request.FILES)
                  print(product_image)
                  
                  new_product = Products.objects.create(product_name=product_name,product_cartegory=product_cartegory,product_price=price,product_description=product_description,product_image=product_image)
                  new_product.save() 
                  return redirect("admin")
            return render(request, 'admin.html', context=context)
      else:
            return redirect('admin-login')
      
def admin_profile(request):
      if request.user.is_authenticated:
            email = request.user.email
            address = request.user.address
            phone = request.user.phone_number
            user = Customers.objects.get(username=request.user)
            orders = Orders.objects.filter(order_user=user)
            # print(address)
            context={
                  'email':email,
                  'address':address,
                  'phone':phone,
                  'username':request.user.username[:5],
                  'orders':orders,
            }
            return render(request, 'administrator/admin_profile.html', context=context)
      
def delete(request):
      if request.method == 'POST':
            product_id = request.POST['product_id']
            print(product_id)
            product = Products.objects.get(product_id=product_id)
            product.delete()
            messages.info(request,  'Product deleted successfully')
            return redirect('admin')    
      
      
def update(request):
      if request.method == 'POST':
            product_id = request.POST['product_id']
            product = Products.objects.get(product_id=product_id)
            product.product_name = request.POST['product_name']
            product.product_price = request.POST['price']
            product.product_description = request.POST['product_description']
            product.product_cartegory = request.POST['cartegory']
            product.product_image = request.FILES.get('image')
            product.save()
            messages.info(request, 'product updated successfully')
            return redirect('admin')


def service(request):
      if request.user.is_authenticated:
            try:
                  data = serializers.serialize("python",Products.objects.all() )
                  # data = Products.objects.all() 
                  items_on_cart =  Cart.objects.all().filter(cart_user_id=request.user.Customer_id)
            except Cart.DoesNotExist:
                  context = {'data':data,
                        'username':request.user.username[:5]
                        }
                  return  render(request, 'userpage.html',context)
            finally:
                  # items_on_cart = Cart.objects.count()
                  context = {'data':data,
                             'items_on_cart':items_on_cart.count(),
                              'username':request.user.username[:5]
                              }
            return render(request, 'service.html',context=context)
      else:
            return render(request, 'service.html')
def contacts(request):
      if request.user.is_authenticated:
            try:
                  data = serializers.serialize("python",Products.objects.all() )
                  # data = Products.objects.all() 
                  items_on_cart =  Cart.objects.all().filter(cart_user_id=request.user.Customer_id)
            except Cart.DoesNotExist:
                  context = {'data':data,
                        'username':request.user.username[:5]
                        }
                  return  render(request, 'userpage.html',context)
            finally:
                  # items_on_cart = Cart.objects.count()
                  context = {'data':data,
                             'items_on_cart':items_on_cart.count(),
                              'username':request.user.username[:5]
                              }
            return render(request, 'contact.html',context=context)
      else:
            return render(request, 'contact.html')

def about(request):
      if request.user.is_authenticated:
            try:
                  data = serializers.serialize("python",Products.objects.all() )
                  # data = Products.objects.all() 
                  items_on_cart =  Cart.objects.all().filter(cart_user_id=request.user.Customer_id)
            except Cart.DoesNotExist:
                  context = {'data':data,
                        'username':request.user.username[:5]
                        }
                  return  render(request, 'userpage.html',context)
            finally:
                  # items_on_cart = Cart.objects.count()
                  context = {'data':data,
                             'items_on_cart':items_on_cart.count(),
                              'username':request.user.username[:5]
                              }
            return render(request, 'about.html',context=context)
      else:
            return render(request, 'about.html')

def cart(request):
      # items to sum up
      def get_total_cart_amount():
            total_amount = Cart.objects.filter(cart_user_id=request.user.Customer_id).aggregate(total=Sum('cart_amount'))['total']
            return total_amount or 0
      # print(get_total_cart_amount(request.user.Customer_id))
      total_sum =  get_total_cart_amount()
      print(total_sum)
      
      if request.user.is_authenticated:
            name = request.user.username[:5]
            try:
                  user = Customers.objects.get(Customer_id=request.user.Customer_id)
                  cart_item =  Cart.objects.all().filter(cart_user=user)
                  
                  print(cart_item)
            except Cart.DoesNotExist:
                  messages.info(request, 'your cart is empty')
                  return render(request, 'cart.html', )
                        
            
            
            
            
            items_on_cart = Cart.objects.all().filter(cart_user_id=request.user.Customer_id).count()
            context = {'items_on_cart':items_on_cart,
                  'cart_item':cart_item,
                  'username':name,
                  'total':total_sum,
                  }
      return render(request, 'Cart.html', context=context)





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
            if Cart.objects.filter(cart_user=customer, cart_product=product).exists():
                messages.info(request, 'Product already added to cart, check your cart to increase the quantity')
                return render(request, 'userpage.html')
            else:
                # Create a new cart item
                newcart = Cart.objects.create(
                    cart_user=customer,
                    cart_product = product
                )
                
                newcart.save()
                messages.success(request, 'Product successfully added to cart')
                return redirect('userpage')
      else:
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
      
            cart_object = Cart.objects.get(cart_user=customer, cart_id=cart_id)
            # if cart_objects.cart_user_id == customer.Customer_id and cart_objects.cart_id == cart_id:
                  # new_object = Cart.objects.get(cart_user_id=customer.Customer_id, cart_id=cart_id)
            cart_object.quantity += 1
            cart_object.cart_amount = cart_object.cart_product.product_price* cart_object.quantity
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
      
            cart_object = Cart.objects.get(cart_user=customer, cart_id=cart_id)
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
            cart_id = request.POST.get('cart_id')
            print(cart_id)
            cart_object = Cart.objects.get(cart_user_id=customer.Customer_id, cart_id=cart_id)
            cart_object.delete()
            messages.success(request,  "Product deleted successfully")
            message_text = "Product deleted successfully"
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                  return JsonResponse({'success': True,'message': message_text,})
      return redirect('cart')


###==========================================######
#           P A Y M E N T S
#============================================######

def payments(request):
      if request.user.is_authenticated:
             # items to sum up
            def get_total_cart_amount():
                  total_amount = Cart.objects.filter(cart_user_id=request.user.Customer_id).aggregate(total=Sum('cart_amount'))['total']
                  return total_amount or 0
            total_sum =  get_total_cart_amount()
            name = request.user
            phone_number  = request.user.phone_number
            momoUser = str(uuid.uuid4())
            # print(momoUser)
            
            # CREATING API USER
            UserHeaders = {'Accept': '*/*',
                  'Content-Type': 'application/json',
                  'X-Reference-Id': momoUser,
                  'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',}
            data={
                  "providerCallbackHost": "https://webhook.site/fc2a2731-9a9b-476e-a40c-5aabf5592dd3"
                  }
            r = requests.post('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser',json=data, headers = UserHeaders)
            print("User Status: ", r.json)
            
            
            # CREATING APIKEY FOR THE CREATED USER
            headersApi = {'Accept': '*/*',
                 'Content-Type': 'application/json',
                 'Ocp-Apim-Subscription-Key': '3edd8df4a822438297e3ef23e70c3aca',
                        }
      
            params={
                  'X-Reference-Id': momoUser
            }
      
            ApiKey = requests.post('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{}/apikey'.format(momoUser),headers = headersApi)
            KEY = ApiKey.text[11:-2]
            print(KEY)
            
            # num= "04f4a2ed646845f2b0923f079d93de16"
            
            # CREATING ACCESS TOKEN FOR THE USER  =====> WE USE THE APIKEY AND THE USERID
            auth_string = f"{momoUser}:{KEY}"
            auth_b64 = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
            athkey = f"Basic {auth_b64}"
            print(athkey)
            headerstoken = {'Accept': '*/*',
                  'Content-Type': 'application/json',
                  'Ocp-Apim-Subscription-Key': '55d237aeb9b04db59cbeb8751f6e8df4',
                  'Authorization': athkey,
                  #      "apiKey":"30dae6e8bb7743d7b7b186c413ad8569"
            }      
            response = requests.post('https://sandbox.momodeveloper.mtn.com/collection/token/', headers = headerstoken)
            AccessToken = response.json()
            print(AccessToken)
            # print(AccessToken['access_token'])
            
            
            # REQUEST TO PAY 
            transactionId = str(uuid.uuid4())
            headersPay = {'Accept': '*/*',
                 'Content-Type': 'application/json',
                 'Ocp-Apim-Subscription-Key': '55d237aeb9b04db59cbeb8751f6e8df4',
                 'Authorization':"Bearer {}".format(AccessToken['access_token']),
                 'X-Reference-Id': transactionId,  #THIS IS FORTHE TRASACTION NOT FOR THE CREATED USER 
            #      'X-Callback-Url': "https://webhook.site/fc2a2731-9a9b-476e-a40c-5aabf5592dd3",
                 'X-Target-Environment': "sandbox"
            }
            amount = str(total_sum)
            print(type(amount))
            body={
                  "amount": amount,
                  "currency": "EUR",#code for UGX
                  "externalId": "12345678",
                  "payer": {
                        "partyIdType": "MSISDN",
                        "partyId": "12345678"
                  },
                  "payerMessage": "testing",
                  "payeeNote": "testing1"
                  }
            requestToPay = requests.post('https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay',json=body, headers = headersPay)
            print(requestToPay)
            
           
            # print(get_total_cart_amount(request.user.Customer_id))
            
            print(amount)
            
      return render(request, 'cart.html')



###==========================================######
#          C H E C K  O U T
#============================================######
def check_out(request):
      if request.user.is_authenticated:
        payments(request)
        
        
        
        customer = Customers.objects.get(username=request.user)
        cart_objects = Cart.objects.filter(cart_user_id=request.user.Customer_id)
        
        with transaction.atomic():
            for cart_item in cart_objects:
                order, created = Orders.objects.get_or_create(
                    order_user=customer,
                    cart=cart_item
                )
                if created:
                    print(f'New order created for cart item: {cart_item}')
                else:
                    print(f'Order already exists for cart item: {cart_item}')

            #   # Clear the user's cart after creating orders
            #   cart_objects.delete()

        print("Checkout completed successfully")
      else:
        print("User is not authenticated", status=401)  
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
                  username=user.username[:5]
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
      if request.user.is_authenticated:
                
            if request.method == "POST":
                  email = request.POST["email"]
                  print(email)
                  
            if News_letter.objects.filter(email=email).exists():
                  messages.info(request,"email already exists")
            else:
                  new = News_letter.objects.create(email=email)
                  new.save()
                  messages.info(request, "Thank you for Subscribing")
            return redirect('userpage')
      else:
            if request.method == "POST":
                  email = request.POST["email"]
                  print(email)
                  
            if News_letter.objects.filter(email=email).exists():
                  messages.info(request,"email already exists")
            else:
                  new = News_letter.objects.create(email=email)
                  new.save()
                  messages.info(request, "Thank you for Subscribing")
            return render(request,'index.html')
      
# =============S E N D   AN   E M A I L==========
def Send_email(request):
      if request.user.is_authenticated:
            try:
                  password = 'hhyx mfca zpvo ckof'
                  if request.method == "POST":
                        subject = request.POST["sub"]
                        message = request.POST["mes"]
                        sender_email = request.POST["your_email"]


                        server_email = 'eliaakjtrnq@gmail.com'
                        email_password = password
                        subject = subject
                        email_receiver = 'eliatranquil@gmail.com'
                        body =  "{}  \n Reply to {}".format(message,sender_email)

                        em = EmailMessage()
                        em['from'] = server_email
                        em['To'] = email_receiver
                        em['subject'] = subject
                        em.set_content(body)

                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                              smtp.login(server_email, email_password)
                              smtp.sendmail(server_email, email_receiver, em.as_string())
                        messages.info(request, "S U C C E S S  !!  Your Message has been Successfully sent, we will respond ASAP")
                        return redirect('userpage')
            except Exception as e:
                  messages.error(request,'Error, Check your Internet connection and try again')
                  return redirect('userpage')       
      else:
            try:
                  password = 'hhyx mfca zpvo ckof'
                  if request.method == "POST":
                        subject = request.POST["sub"]
                        message = request.POST["mes"]
                        sender_email = request.POST["your_email"]


                        server_email = 'eliaakjtrnq@gmail.com'
                        email_password = password
                        subject = subject
                        email_receiver = 'eliatranquil@gmail.com'
                        body =  "{}  \n Reply to {}".format(message,sender_email)

                        em = EmailMessage()
                        em['from'] = server_email
                        em['To'] = email_receiver
                        em['subject'] = subject
                        em.set_content(body)

                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                              smtp.login(server_email, email_password)
                              smtp.sendmail(server_email, email_receiver, em.as_string())
                        messages.info(request, "S U C C E S S  !!! Your Message has been Successfully sent, we will respond ASAP")
                        render(request,'contact.html')
            except Exception as e:
                  print(e)
                  messages.error(request,'Error, Check your Internet connection and try again')
                  return render(request,'contact.html')
      return  render(request,'contact.html')
            
def detail(request, pk):
      detail = Products.objects.get(product_id=pk)
      return render(request, 'preview.html', {'detail': detail})

def gallery(request):
      if request.method =="POST":
            image = request.FILES.get('image')
            title = request.POST['title']
            Gallery.objects.create(title=title, image=image)
            messages.success(request, "Image uploaded successfully")
      return redirect('admin')
                  
def get_gallery(request):
      if request.user.is_authenticated:
            try:
                  items_on_cart =  Cart.objects.all().filter(cart_user_id=request.user.Customer_id)
            except Cart.DoesNotExist:
                  context = {
                        'username':request.user.username[5]
                        }
                  return  render(request, 'userpage.html',context)
            finally:
                  # items_on_cart = Cart.objects.count()
                  context = {
                             
                              }
            gallery_object = Gallery.objects.all()
            Product_object = Products.objects.all()
            print(gallery_object)
            context ={
            'items_on_cart':items_on_cart.count(),
            'username':request.user.username[:5],
            'gallery': gallery_object,
            'product': Product_object
            }
            return render(request, "gallery.html", context=context)
      else:
            gallery_object = Gallery.objects.all()
            Product_object = Products.objects.all()
            new_context = {
            'gallery': gallery_object,
            'product': Product_object
            }
            return render(request, "gallery.html", context=new_context)
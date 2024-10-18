from django.shortcuts import render, redirect
from gold.models import News_letter, Customers,Products,Orders
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core import serializers



def index(request):
      
      data = serializers.serialize("python",Products.objects.all() )
      print(data)
      context = {'data':data,} 
      
      return  render(request, 'index.html',context=context)

def admin(request):
      if request.method == 'POST':
            product_name = request.POST['product_name']
            price = request.POST['price']
            product_description  = request.POST['product_description']
            product_image = request.FILES.get('image')
            
            # print(request.FILES)
            print(product_image)
            
            new_product = Products.objects.create(product_name=product_name,product_price=price,product_description=product_description,product_image=product_image)
            new_product.save()    
            



      return render(request, 'admin.html')

def make_order(request, pk):
      product = Products.objects.get(id=pk)
      customer = Customers.objects.get(id=request.user.id)
      order = Orders.objects.create(customer=customer,product=product)
      order.save()
      return redirect('index')
      pass

def service(request):
    return render(request, 'service.html')

def contacts(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def Add_Item_to_cart(request):
      
    return render(request, 'room.html')


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
                  return render(request,'index.html', {'username': username.capitalize()})
                  
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
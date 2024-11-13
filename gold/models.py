from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager

class News_letter(models.Model):
    email = models.EmailField(blank=True,default=None)
    
class Admin(models.Model):
      email = models.EmailField(unique=True)
      username = models.CharField(max_length=100,unique=True)
      password = models.CharField(max_length=100)
      

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})
  
class Customers(AbstractBaseUser , PermissionsMixin):
      
      username = models.CharField(max_length=100,unique=True)
      Customer_id = models.CharField(max_length=255,primary_key=True,unique=True)
      def save(self, *args, **kwargs):
        if not self.Customer_id:  # Only generate if no ID is set
            # Get the last object inserted to determine the next ID
            last_object = Customers.objects.all().order_by('Customer_id').last()

            if last_object:
                # Extract the number from the last ID and increment it
                last_id = last_object.Customer_id
                number = int(last_id[5:]) + 1
                new_id = f'CUST-{str(number).zfill(3)}'
            else:
                new_id = 'CUST-001'  # Start with 'fxx001' if no object exists
            
            self.Customer_id = new_id

        super(Customers, self).save(*args, **kwargs)
      email = models.EmailField(blank=True, default=None)
      password = models.CharField(max_length=255,)
      phone_number = models.CharField(max_length=20, blank=True, default=None)
      address = models.CharField(max_length=255, blank=True, default=None)
      USERNAME_FIELD = 'username'  # or whatever field you want to use as the username
      REQUIRED_FIELDS = ['email', 'password','phone_number']
      objects = CustomUserManager()

     
class Products(models.Model):
      product_image = models.ImageField(upload_to='products')
      product_id = models.AutoField(primary_key=True,unique=True)
      product_name = models.CharField(max_length=255)
      product_price = models.DecimalField(max_digits=10, decimal_places=2)
      product_description = models.CharField(max_length=255)
      product_cartegory = models.CharField(max_length=255,default='breakfast')

class Orders(models.Model):
      order_id = models.CharField(max_length=255,primary_key=True)
      customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
      product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
      Order_date = models.DateTimeField()
      Total_cost = models.DecimalField(decimal_places=2, max_digits=10)
      status = models.BooleanField(default=False)
      
class Cart(models.Model):
      cart_id = models.AutoField(primary_key=True, unique=True,default=None)
      cart_user = models.ForeignKey(to=Customers, on_delete=models.CASCADE)
      Product_id = models.IntegerField(default=None)
      Cart_image = models.ImageField(upload_to='cart/')
      Cart_name = models.CharField(max_length=255)
      Cart_price = models.DecimalField(max_digits=10, decimal_places=2)            
      Cart_description = models.CharField(max_length=255)
      quantity = models.IntegerField(default=1)
      Cart_amount = models.IntegerField(default=1)
      def save(self, *args, **kwargs):
        # Update Cart_amount based on Cart_price and quantity
        self.Cart_amount = self.Cart_price * self.quantity
        super(Cart,self).save(*args, **kwargs)
      
class Payments(models.Model):
      payment_id = models.CharField(max_length=255,primary_key=True)
      customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
      order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
      payment_date = models.DateTimeField()
      Amount = models.DecimalField(decimal_places=2,max_digits=10)
      
      
      
      
            
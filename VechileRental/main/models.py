from django.db import models

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Vehicle(models.Model):
 
    Vehicle_name = models.CharField(max_length=60)
    Vehicle_company = models.CharField(max_length=60)
    Vehicle_color = models.CharField(max_length=20)
    Vehicle_image1 = models.ImageField(upload_to='img/Vehicle_images/')
    Vehicle_image2 = models.ImageField(upload_to='img/Vehicle_images/')
    Vehicle_image3 = models.ImageField(upload_to='img/Vehicle_images/')
    Vehicle_description = models.CharField(max_length=1500)
    Vehicle_price = models.IntegerField()

    def __str__(self):
        return str(self.Vehicle_name)


# customer model
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    customer_firstname = models.CharField(max_length=60)
    customer_lastname = models.CharField(max_length=60)
    customer_address = models.CharField(max_length=600)
    customer_email = models.EmailField(max_length=100)
    customer_dob = models.DateField()
    customer_mobileno = models.CharField(max_length=15)  
    customer_license = models.ImageField(upload_to='img/Customer_License/')
    order_take_day = models.DateField(default=None)
    order_return_day = models.DateField(default=None)  

    def __str__(self):
        return f"{self.customer_email} | License: {self.customer_license.name}"
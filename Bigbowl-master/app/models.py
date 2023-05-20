from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES= (
    ('Bihar','Bihar'),
    ('Jharkhand','Jharkhand'),
    ('Uttar pradesh','Uttar pradesh'),
    ('Madhya pradesh','Madhya pradesh'),
    ('Gujrat','Gujrat'),
    ('Hayana','Hayana'),
    ('Panjab','Panjab'),
    ('Himachal pradesh','Himachal pradesh'),
)
class Customer(models.Model):
    username =models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality= models.CharField(max_length=200)
    city= models.CharField(max_length=50)
    zipcode= models.IntegerField()
    state= models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)


CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','TopWear'),
    ('BW','BottomWear'),
    ('S','SmartWatch'),

)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    actual_price = models.FloatField()
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','on the way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)
class PlacedOrdered(models.Model):
    username=  models.ForeignKey(User, on_delete=models.CASCADE)
    customer=  models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=  models.PositiveIntegerField(default=1)
    order_date= models.DateTimeField(auto_now_add= True)
    status= models.CharField(max_length=50, choices= STATUS_CHOICES,default='Pending')

from unicodedata import category
from django.contrib import messages
from django.shortcuts import  render
from django.contrib.auth.models import User,auth
from django.views import View
from .models import Customer, PlacedOrdered,Product,Cart
from .forms import CustomerRegistrationForm


class ProductView(View):
    def get(self, request):
        topwear= Product.objects.filter(category='TW')
        bottomwear= Product.objects.filter(category='BW')
        mobile= Product.objects.filter(category='M')
        laptop= Product.objects.filter(category='L')
        smartwatch=Product.objects.filter(category='S')
        return render(request,'app/home.html',{'topwear': topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop,'smartwatch':smartwatch})

class ProductDetailsView(View):
    def get(self, request, pk):
        product= Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# ====================================================mobile filter =====================================
def mobile(request,data=None):
    if data == None:
        mobile= Product.objects.filter(category='M')
    elif data == 'MI' or data=='Samsung' or data=='Realme'or data=='vivo' or data=='OOPO':
        mobile= Product.objects.filter(category='M').filter(brand=data)
    elif data =='below':
        mobile= Product.objects.filter(category='M').filter(actual_price__lt=10000)
    elif data =='above':
        mobile= Product.objects.filter(category='M').filter(actual_price__gt=10000)
    return render(request, 'app/mobile.html',{'mobile':mobile})


# ======================================================laptop filter ==============================================/

def laptop(request,data=None):
    if data== None:
        laptop= Product.objects.filter(category='L')
    elif data == data=='Asus' or data=='Hp'or data=='Lenovo' or data=='Dell' or data== 'Hp' or data== 'Honor':
        laptop= Product.objects.filter(category='L').filter(brand=data)
    elif data =='below':
        laptop= Product.objects.filter(category='L').filter(actual_price__lt=30000)
    elif data =='above':
        laptop= Product.objects.filter(category='L').filter(actual_price__gt=30000)
    return render(request, 'app/laptop.html',{'laptop':laptop})



# ================================================ topwears==============================
def topWear(request,data=None):
    if data == None:
        topwear= Product.objects.filter(category='TW')
    elif data == 'Tokyo' or data=='Roadster' or data=='Spark':
        topwear= Product.objects.filter(category='TW').filter(brand=data)
    elif data =='below':
        topwear= Product.objects.filter(category='TW').filter(actual_price__lt=10000)
    elif data =='above':
        topwear= Product.objects.filter(category='TW').filter(actual_price__gt=10000)
    return render(request, 'app/topwear.html',{'topwear':topwear})

    
# ================================================ botthomwear ==========================
def bottomWear(request,data=None):
    if data == None:
        bottomwear= Product.objects.filter(category='BW')
    elif data == 'Tokyo' or data=='Roadster' or data=='Q-Rious' or data =='Spark':
        bottomwear= Product.objects.filter(category='BW').filter(brand=data)
    elif data =='below':
        bottomwear= Product.objects.filter(category='BW').filter(actual_price__lt=10000)
    elif data =='above':
        bottomwear= Product.objects.filter(category='BW').filter(actual_price__gt=10000)
    return render(request, 'app/bottomwear.html',{'bottomwear':bottomwear})

    # =========================================smartwatch=======================================
def smartwatch(request,data=None):
    if data == None:
        smartwatch= Product.objects.filter(category='S')
    elif data == 'Boat' or data=='Samsung' or data=='Realme'or data=='vivo' or data=='OPPO':
        smartwatch= Product.objects.filter(category='S').filter(brand=data)
    elif data =='below':
        smartwatch= Product.objects.filter(category='S').filter(actual_price__lt=10000)
    elif data =='above':
        smartwatch= Product.objects.filter(category='S').filter(actual_price__gt=10000)
    return render(request, 'app/smartwatch.html',{'smartwatch':smartwatch})


# =================================================userRegistraion===============================================

class CustomerRegistrationView(View):
    def get(self,request):
        form= CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self, request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulation ! Registred Successfully")
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})





def checkout(request):
 return render(request, 'app/checkout.html')








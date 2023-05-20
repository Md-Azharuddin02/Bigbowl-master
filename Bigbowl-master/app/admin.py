from django.contrib import admin
from .models import(
    Customer,
    PlacedOrdered,
    Product,
    Cart
)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display= ['id','username','locality','city','zipcode','state']

@admin.register(PlacedOrdered)
class PlaceOrderedModelAdmin(admin.ModelAdmin):
    list_display= ['id','username','customer','product','quantity','order_date','status']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display= ['id','title','selling_price','actual_price','description','brand','category','product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display= ['id','username','product','quantity']


from django.contrib import admin
from .models import Customer,Product,money_item,Video18,Order,ShippingAddress,OrderItem,Entry
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(money_item)
admin.site.register(Video18)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Entry)
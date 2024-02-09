from django.contrib import admin
from .models import *

admin.site.register(Area)
admin.site.register(DeliveryAgency)
admin.site.register(ShopOrderStatus)
admin.site.register(OrderStatus)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAgencyOrders)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['shop', 'first_name', 'last_name', 'email', 'mobile']


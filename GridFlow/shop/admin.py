from django.contrib import admin
from .models import *

admin.site.register(Shop)
admin.site.register(ShopBranch)
admin.site.register(ShopBranchProduct)
admin.site.register(Stock)
admin.site.register(StockAlerts)
admin.site.register(StockAlertTrigger)
admin.site.register(StockAlertGroup)
admin.site.register(StockAlertSubscription)
admin.site.register(StockAlertGroupSubscription)
admin.site.register(ShopRole)


@admin.register(ProductStockLog)
class ShopBranchProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'shop', 'quantity', 'timestamp']

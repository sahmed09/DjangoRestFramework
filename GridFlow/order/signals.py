from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import *
from shop.models import Stock


@receiver(post_save, sender=OrderItem)
def update_stock(sender, created, instance, **kwargs):
    if created:
        stock = Stock.objects.filter(product__slug=instance.product.product.slug).first()
        stock.quantity = stock.quantity - instance.quantity
        stock.save()
        print("Stock updated")

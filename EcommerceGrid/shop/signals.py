from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import channels.layers
from asgiref.sync import async_to_sync


@receiver(post_save, sender=Stock)
def product_stock_log(sender, created, instance, **kwargs):
    ProductStockLog.objects.create(shop=instance.shop.slug, branch=instance.branch.slug, product=instance.product.slug,
                                   quantity=instance.quantity)


@receiver(post_save, sender=Stock)
def trigger(sender, instance, **kwargs):
    try:
        stock_alert = StockAlerts.objects.filter(product__slug=instance.product.slug).first()
        if stock_alert.stock_below < instance.quantity < stock_alert.stock_above:
            print("Alert Triggered!!")
            StockAlertTrigger.objects.create(stock_alert=stock_alert, current_stock=instance.quantity)
    except:
        pass


@receiver(post_save, sender=StockAlertTrigger)
def stock_alert_trigger(sender, created, instance, **kwargs):
    if created:
        stock_alert = instance.stock_alert
        print(stock_alert)
        stock_alert_subscriber = stock_alert.stockalertsubscription_set.all()
        for subscriber in stock_alert_subscriber:
            print(subscriber.user.username)
        print()

        stock_alert_group = StockAlertGroup.objects.filter(stock_alert=stock_alert).first()
        stock_alert_group_subscriber = stock_alert_group.stockalertgroupsubscription_set.all()
        for subscriber in stock_alert_group_subscriber:
            print(subscriber.user.username)


@receiver(post_save, sender=Stock, dispatch_uid='update_status')
def update_status(sender, instance, **kwargs):
    room_name = instance.shop.slug
    room_group_name = 'shop_%s' % room_name

    message = {
        'product': instance.product.name,
        'current stock': instance.quantity,
    }

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type': 'send_message',
            'message': message
        }
    )

from django.db.models.signals import pre_save
from django.dispatch import receiver
from order.models import *
from shop.models import *
from accounting.models import *


@receiver(pre_save, sender=Order)
def order_transaction_trigger(sender, instance, **kwargs):
    order = Order.objects.filter(id=instance.id).first()

    if order is not None:
        shop = instance.customer.shop
        old_status = order.order_status
        new_status = instance.order_status

        otts = OrderTransactionTrigger.objects.filter(shop=shop, from_status=old_status, to_status=new_status)

        for ott in otts:
            from_user = None
            to_user = None

            if ott.from_user == 'me':
                from_user = ShopRole.objects.get(shop=shop, role='SO')
                from_user = TransactionUser.objects.get(user__username=from_user.user)
            elif ott.from_user == 'da':
                from_user = ShopRole.objects.get(shop=shop, role='DA')
                from_user = TransactionUser.objects.get(user__username=from_user.user)
            elif ott.from_user == 'c':
                from_user = ShopRole.objects.get(shop=shop, role='C')
                from_user = TransactionUser.objects.get(user__username=from_user.user)

            if ott.to_user == 'me':
                to_user = ShopRole.objects.get(shop=shop, role='SO')
                to_user = TransactionUser.objects.get(user__username=to_user.user)
            elif ott.to_user == 'da':
                to_user = ShopRole.objects.get(shop=shop, role='DA')
                to_user = TransactionUser.objects.get(user__username=to_user.user)
            elif ott.to_user == 'c':
                to_user = ShopRole.objects.get(shop=shop, role='C')
                to_user = TransactionUser.objects.get(user__username=to_user.user)

            if old_status == ott.from_status and new_status == ott.to_status:
                if ott.transaction_type == 'D':
                    Transaction.objects.create(debit=ott.amount, resolve=True,
                                               credit_from=from_user, debit_to=to_user)
                elif ott.transaction_type == 'C':
                    Transaction.objects.create(credit=ott.amount, resolve=False,
                                               credit_from=from_user, debit_to=to_user)

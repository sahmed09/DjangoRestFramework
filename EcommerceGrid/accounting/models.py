from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TransactionUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class Transaction(models.Model):
    credit = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    debit = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    resolve = models.BooleanField(default=False)
    credit_from = models.ForeignKey(TransactionUser, on_delete=models.SET_NULL, null=True, related_name='credit')
    debit_to = models.ForeignKey(TransactionUser, on_delete=models.SET_NULL, null=True, related_name='debit')
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.credit_from} - {self.debit_to} - {self.date_time}'


class OrderTransactionTrigger(models.Model):
    TRANSACTION_TYPE = (
        ('D', 'Debit'),
        ('C', 'Credit')
    )
    USER = (
        ('me', 'me'),
        ('da', 'delivery_agent'),
        ('c', 'customer')
    )
    shop = models.ForeignKey('shop.Shop', on_delete=models.SET_NULL, null=True)
    from_status = models.ForeignKey('order.OrderStatus', on_delete=models.SET_NULL, null=True,
                                    related_name='from_status')
    to_status = models.ForeignKey('order.OrderStatus', on_delete=models.SET_NULL, null=True, related_name='to_status')
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=200)
    from_user = models.CharField(choices=USER, max_length=200)
    to_user = models.CharField(choices=USER, max_length=200)
    resolve = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.shop} - {self.transaction_type} - {self.amount} - {self.resolve}'

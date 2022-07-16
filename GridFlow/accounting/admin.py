from django.contrib import admin
from .models import *

admin.site.register(TransactionUser)
admin.site.register(Transaction)
admin.site.register(OrderTransactionTrigger)

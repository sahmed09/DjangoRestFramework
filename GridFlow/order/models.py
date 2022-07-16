from django.db import models
from django.utils import timezone
from datetime import datetime
from django.utils.text import slugify


def unique_slug(mdl, target_name):
    slug = slugify(target_name)

    check_slug = mdl.objects.filter(slug=slug).exists()
    count = 1
    while check_slug:
        count += 1
        slug = slugify(target_name) + '-' + str(count)
        check_slug = mdl.objects.filter(slug=slug).exists()
    return slug


class Customer(models.Model):
    shop = models.ForeignKey('shop.Shop', on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(null=True, unique=True)
    mobile = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Area(models.Model):
    name = models.CharField(max_length=200)
    parent_area = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True, blank=True)  # self referencing
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(Area, self.name)
        super(Area, self).save(*args, **kwargs)


class DeliveryAgency(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    logo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Delivery Agencies"


class ShopOrderStatus(models.Model):
    shop = models.ForeignKey('shop.Shop', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.shop} - {self.status}'


class OrderStatus(models.Model):
    shop_order_status = models.ForeignKey(ShopOrderStatus, on_delete=models.SET_NULL, null=True, blank=True)
    msg = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.shop_order_status} - {self.msg}'

    class Meta:
        verbose_name_plural = "Order Statuses"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shop = models.ForeignKey('shop.Shop', on_delete=models.SET_NULL, null=True)
    order_status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    transaction_id = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=255, null=False)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer}'

    def save(self, *args, **kwargs):
        if not self.pk:
            transaction_id = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
            transaction_id_hex = hex(int(transaction_id))
            self.transaction_id = transaction_id_hex

        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('shop.ShopBranchProduct', on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.order} - {self.product}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.product_name = self.product.product
            self.price = self.product.price
        # Update order item if order status is pending, using try except, raise an exception if order status is not
        # pending
        order_status = self.order.order_status
        print(order_status)
        # if order_status != 'Pending':
        #     raise ValueError("Can't update")
        #     self.quantity =
        # else:
        #     print("can't do this")
        super(OrderItem, self).save(*args, **kwargs)


class DeliveryAgencyOrders(models.Model):
    agency = models.ForeignKey(DeliveryAgency, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    ordered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.agency} - {self.order}'

    class Meta:
        verbose_name_plural = "Delivery Agency Orders"

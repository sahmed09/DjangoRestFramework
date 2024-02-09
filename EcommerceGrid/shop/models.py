from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


def unique_slug(mdl, target_name):
    slug = slugify(target_name)

    check_slug = mdl.objects.filter(slug=slug).exists()
    count = 1
    while check_slug:
        count += 1
        slug = slugify(target_name) + '-' + str(count)
        check_slug = mdl.objects.filter(slug=slug).exists()
    return slug


class Shop(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)
    album = models.ForeignKey('gallery.Album', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(Shop, self.name)
        super(Shop, self).save(*args, **kwargs)


class ShopBranch(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    album = models.ForeignKey('gallery.Album', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.shop} - {self.name}'

    def save(self, *args, **kwargs):
        if not self.pk:
            shop = self.shop.slug
            slug = unique_slug(ShopBranch, self.name)
            self.slug = shop + '-' + slug
        super(ShopBranch, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Shop Branches"
        unique_together = ('shop', 'name')


class ShopBranchProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    branch = models.ForeignKey(ShopBranch, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.product} - {self.branch}'

    class Meta:
        unique_together = ('shop', 'branch', 'product')


class ShopRole(models.Model):
    ROLE = (
        ('SO', 'Shop Owner'),
        ('C', 'Customer'),
        ('DA', 'Delivery Agent'),
    )

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLE, max_length=200, null=True)

    def __str__(self):
        return f'{self.user} - {self.shop} - {self.role}'

    class Meta:
        unique_together = ('shop', 'user', 'role')


class Stock(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    branch = models.ForeignKey(ShopBranch, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.product} - {self.quantity}'

    class Meta:
        unique_together = ('shop', 'branch', 'product')


class StockAlerts(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    branch = models.ForeignKey(ShopBranch, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stock_below = models.IntegerField()
    stock_above = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name_plural = "Stock Alerts"


class StockAlertTrigger(models.Model):
    stock_alert = models.ForeignKey(StockAlerts, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    current_stock = models.IntegerField()

    def __str__(self):
        return str(self.stock_alert)


class StockAlertGroup(models.Model):
    stock_alert = models.ForeignKey(StockAlerts, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.stock_alert)


class StockAlertSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_alert = models.ForeignKey(StockAlerts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stock_alert} - {self.user}'


class StockAlertGroupSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_alert_group = models.ForeignKey(StockAlertGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.stock_alert_group} - {self.user}'


class ProductStockLog(models.Model):
    shop = models.CharField(max_length=255)
    branch = models.CharField(max_length=255, null=True, blank=True)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.shop} - {self.product} - {self.quantity}'

    class Meta:
        ordering = ['-timestamp']

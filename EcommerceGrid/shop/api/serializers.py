from django.shortcuts import get_object_or_404
from rest_framework import serializers
from shop.models import *
from django.contrib.auth.models import User
from gallery.models import Album
from store.models import Product
from store.api.serializers import ProductSerializerSummary


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
        read_only_fields = ['slug']

    def to_internal_value(self, data):
        if data.get('album'):
            self.fields['album'] = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

            album_name = data['album']['name']
            album = get_object_or_404(Album, name=album_name)

            data['album'] = album.id

        return super(ShopSerializer, self).to_internal_value(data)


class ShopBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopBranch
        fields = '__all__'
        read_only_fields = ['slug']

    def to_internal_value(self, data):
        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        if data.get('album'):
            self.fields['album'] = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

            album_name = data['album']['name']
            album = get_object_or_404(Album, name=album_name)

            data['album'] = album.id

        return super(ShopBranchSerializer, self).to_internal_value(data)


class ShopSerializerSummary(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'slug']
        read_only_fields = ['slug']


class ShopBranchSerializerSummary(serializers.ModelSerializer):
    class Meta:
        model = ShopBranch
        fields = ['name', 'slug']
        read_only_fields = ['slug']


class ShopBranchProductSerializer(serializers.ModelSerializer):
    product = ProductSerializerSummary()
    shop = ShopSerializerSummary()
    branch = ShopBranchSerializerSummary()

    class Meta:
        model = ShopBranchProduct
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        if data.get('branch'):
            self.fields['branch'] = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

            branch_slug = data['branch']['slug']
            branch = get_object_or_404(ShopBranch, slug=branch_slug)

            data['branch'] = branch.id

        if data.get('product'):
            self.fields['product'] = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

            product_slug = data['product']['slug']
            product = get_object_or_404(Product, slug=product_slug)

            data['product'] = product.id

        return super(ShopBranchProductSerializer, self).to_internal_value(data)


class UserSerializerSummary(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ShopRoleSerializer(serializers.ModelSerializer):
    shop = ShopSerializerSummary()
    user = UserSerializerSummary()

    class Meta:
        model = ShopRole
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('user'):
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

            username = data['user']['username']
            user = get_object_or_404(User, username=username)

            data['user'] = user.id

        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        return super(ShopRoleSerializer, self).to_internal_value(data)


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializerSummary()

    class Meta:
        model = Stock
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        if data.get('branch'):
            self.fields['branch'] = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

            branch_slug = data['branch']['slug']
            branch = get_object_or_404(ShopBranch, slug=branch_slug)

            data['branch'] = branch.id

        if data.get('product'):
            self.fields['product'] = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

            product_slug = data['product']['slug']
            product = get_object_or_404(Product, slug=product_slug)

            data['product'] = product.id

        return super(StockSerializer, self).to_internal_value(data)


class StockAlertsSerializer(serializers.ModelSerializer):
    product = ProductSerializerSummary()

    class Meta:
        model = StockAlerts
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        if data.get('branch'):
            self.fields['branch'] = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

            branch_slug = data['branch']['slug']
            branch = get_object_or_404(ShopBranch, slug=branch_slug)

            data['branch'] = branch.id

        if data.get('product'):
            self.fields['product'] = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

            product_slug = data['product']['slug']
            product = get_object_or_404(Product, slug=product_slug)

            data['product'] = product.id

        return super(StockAlertsSerializer, self).to_internal_value(data)


class StockAlertsSerializerSummary(serializers.ModelSerializer):
    class Meta:
        model = StockAlerts
        fields = ['name', 'description']


class StockAlertGroupSerializer(serializers.ModelSerializer):
    stock_alert = StockAlertsSerializerSummary()

    class Meta:
        model = StockAlertGroup
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('stock_alert'):
            self.fields['stock_alert'] = serializers.PrimaryKeyRelatedField(queryset=StockAlerts.objects.all())

            stock_alert_name = data['stock_alert']['name']
            stock_alert = get_object_or_404(StockAlerts, name=stock_alert_name)

            data['stock_alert'] = stock_alert.id

        return super(StockAlertGroupSerializer, self).to_internal_value(data)


class StockAlertSubscriptionSerializer(serializers.ModelSerializer):
    stock_alert = StockAlertsSerializerSummary()
    user = UserSerializerSummary()

    class Meta:
        model = StockAlertSubscription
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('stock_alert'):
            self.fields['stock_alert'] = serializers.PrimaryKeyRelatedField(queryset=StockAlerts.objects.all())

            stock_alert_name = data['stock_alert']['name']
            stock_alert = get_object_or_404(StockAlerts, name=stock_alert_name)

            data['stock_alert'] = stock_alert.id

        if data.get('user'):
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

            username = data['user']['username']
            user = get_object_or_404(User, username=username)

            data['user'] = user.id

        return super(StockAlertSubscriptionSerializer, self).to_internal_value(data)


class StockAlertGroupSubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializerSummary()

    class Meta:
        model = StockAlertGroupSubscription
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('user'):
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

            username = data['user']['username']
            user = get_object_or_404(User, username=username)

            data['user'] = user.id

        return super(StockAlertGroupSubscriptionSerializer, self).to_internal_value(data)


class ProductStockLogSerializer(serializers.ModelSerializer):
    date = serializers.CharField()
    max_quantity = serializers.IntegerField()
    min_quantity = serializers.IntegerField()
    avg_quantity = serializers.FloatField()

    class Meta:
        model = ProductStockLog
        fields = ['date', 'max_quantity', 'min_quantity', 'avg_quantity']

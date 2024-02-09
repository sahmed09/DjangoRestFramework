from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.models import User
from order.models import *
from shop.models import ShopBranchProduct, Shop
from shop.api.serializers import ShopSerializerSummary


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        return super(CustomerSerializer, self).to_internal_value(data)


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('parent_area'):
            self.fields['parent_area'] = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())

            p_area_slug = data['parent_area']['slug']
            p_area = get_object_or_404(Area, slug=p_area_slug)

            data['parent_area'] = p_area.id

        return super(AreaSerializer, self).to_internal_value(data)


class DeliveryAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgency
        fields = '__all__'


class ShopOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopOrderStatus
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        return super(ShopOrderStatusSerializer, self).to_internal_value(data)


class ShopOrderStatusSerializerSummary(serializers.ModelSerializer):
    class Meta:
        model = ShopOrderStatus
        fields = ['status']


class OrderStatusSerializer(serializers.ModelSerializer):
    shop_order_status = ShopOrderStatusSerializerSummary()

    class Meta:
        model = OrderStatus
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('shop_order_status'):
            self.fields['shop_order_status'] = serializers.PrimaryKeyRelatedField(queryset=ShopOrderStatus.objects.all())

            status_name = data['shop_order_status']['status']
            status = get_object_or_404(ShopOrderStatus, status=status_name)

            data['shop_order_status'] = status.id
        return super(OrderStatusSerializer, self).to_internal_value(data)


class CustomerSerializerSummary(serializers.ModelSerializer):
    shop = ShopSerializerSummary()

    class Meta:
        model = Customer
        fields = ['id', 'shop', 'mobile']


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializerSummary()
    shop = ShopSerializerSummary()

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['transaction_id']

    def to_internal_value(self, data):
        if data.get('customer'):
            self.fields['customer'] = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

            mobile = data['customer']['mobile']
            customer = get_object_or_404(Customer, mobile=mobile)

            data['customer'] = customer.id

        if data.get('shop'):
            self.fields['shop'] = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())

            shop_slug = data['shop']['slug']
            shop = get_object_or_404(Shop, slug=shop_slug)

            data['shop'] = shop.id

        if data.get('order_status'):
            self.fields['order_status'] = serializers.PrimaryKeyRelatedField(queryset=OrderStatus.objects.all())

            status_name = data['order_status']['shop_order_status']['status']
            status = get_object_or_404(OrderStatus, shop_order_status__status=status_name)

            data['order_status'] = status.id

        if data.get('area'):
            self.fields['area'] = serializers.PrimaryKeyRelatedField(queryset=Area.objects.all())

            area_slug = data['area']['slug']
            area = get_object_or_404(Area, slug=area_slug)

            data['area'] = area.id

        return super(OrderSerializer, self).to_internal_value(data)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('product'):
            self.fields['product'] = serializers.PrimaryKeyRelatedField(queryset=ShopBranchProduct.objects.all())

            product_slug = data['product']['product']['slug']
            product = get_object_or_404(ShopBranchProduct, product__slug=product_slug)

            data['product'] = product.id

        if data.get('order'):
            self.fields['order'] = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

            transaction_id = data['order']['transaction_id']
            order = get_object_or_404(Order, transaction_id=transaction_id)

            data['order'] = order.id

        return super(OrderItemSerializer, self).to_internal_value(data)


class DeliveryAgencyOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgencyOrders
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('agency'):
            self.fields['agency'] = serializers.PrimaryKeyRelatedField(queryset=DeliveryAgency.objects.all())

            agency_name = data['agency']['name']
            agency = get_object_or_404(DeliveryAgency, name=agency_name)

            data['agency'] = agency.id

        if data.get('order'):
            self.fields['order'] = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())

            transaction_id = data['order']['transaction_id']
            order = get_object_or_404(Order, transaction_id=transaction_id)

            data['order'] = order.id

        return super(DeliveryAgencyOrdersSerializer, self).to_internal_value(data)

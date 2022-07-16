from django.contrib.auth.models import User
from django.db.models import Q
from order.models import *
from order.api.serializers import *
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()


class CustomerModelViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['email', 'mobile', 'shop__slug']


class AreaModelViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['slug', 'parent_area__slug']


class DeliveryAgencyModelViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAgency.objects.all()
    serializer_class = DeliveryAgencySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']


class ShopOrderStatusModelViewSet(viewsets.ModelViewSet):
    queryset = ShopOrderStatus.objects.all()
    serializer_class = ShopOrderStatusSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['status', 'shop__slug']


class OrderStatusModelViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['shop_order_status__status', 'shop_order_status__shop__slug']


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['mobile', 'transaction_id', 'order_status__shop_order_status__status']

    def get_queryset(self):
        queryset = super(OrderModelViewSet, self).get_queryset()

        area = self.request.query_params.get('area')
        if area:
            queryset = queryset.filter(Q(area__parent_area__name__in=[area]) | Q(area__name__in=[area]))

        return queryset


class OrderItemModelViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['order__transaction_id']


class DeliveryAgencyOrdersModelViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAgencyOrders.objects.all()
    serializer_class = DeliveryAgencyOrdersSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['agency__name', 'order__transaction_id']

    def create(self, request, *args, **kwargs):
        agency = request.query_params.get('agency')
        agency = DeliveryAgency.objects.filter(name__icontains=agency).first()

        message = {}

        for data in request.data['data']:

            order = Order.objects.filter(transaction_id=data['transaction_id']).first()

            if not DeliveryAgencyOrders.objects.filter(order=order).exists():
                DeliveryAgencyOrders.objects.create(agency=agency, order=order)
                message = {"message": "Delivery Agency Assigned Successfully"}
            else:
                message = {"message": "Delivery Agency For this order already exists"}

        return Response(message)

#    if agency is not None:

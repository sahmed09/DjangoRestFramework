from shop.models import *
from shop.api.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import mixins
from django.db.models import Max, Avg, Min
import pytz
from django.db.models.functions import TruncMonth, TruncYear, TruncDate


class ShopModelViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['slug']


class ShopBranchModelViewSet(viewsets.ModelViewSet):
    queryset = ShopBranch.objects.all()
    serializer_class = ShopBranchSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['shop__slug']


class ShopBranchProductModelViewSet(viewsets.ModelViewSet):
    queryset = ShopBranchProduct.objects.all()
    serializer_class = ShopBranchProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['shop__slug', 'branch__slug', 'product__slug']


class ShopRoleModelViewSet(viewsets.ModelViewSet):
    queryset = ShopRole.objects.all()
    serializer_class = ShopRoleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['shop__slug', 'role']


class StockModelViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['shop__slug', 'branch__slug', 'product__slug']


class StockAlertsModelViewSet(viewsets.ModelViewSet):
    queryset = StockAlerts.objects.all()
    serializer_class = StockAlertsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['product__slug']


class StockAlertGroupModelViewSet(viewsets.ModelViewSet):
    queryset = StockAlertGroup.objects.all()
    serializer_class = StockAlertGroupSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class StockAlertSubscriptionModelViewSet(viewsets.ModelViewSet):
    queryset = StockAlertSubscription.objects.all()
    serializer_class = StockAlertSubscriptionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class StockAlertGroupSubscriptionModelViewSet(viewsets.ModelViewSet):
    queryset = StockAlertGroupSubscription.objects.all()
    serializer_class = StockAlertGroupSubscriptionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ProductStockLogListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductStockLogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    queryset = ProductStockLog.objects.all()

    def get_queryset(self):
        queryset = super(ProductStockLogListViewSet, self).get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        interval = self.request.query_params.get('interval')
        shop = self.request.query_params.get('shop', '')
        branch = self.request.query_params.get('branch', '')
        product = self.request.query_params.get('product', '')

        if start_date:
            if interval == 'daily':
                queryset = queryset.annotate(
                    date=TruncDate('timestamp', tzinfo=pytz.UTC)
                ).values(
                    'date'
                ).extra(
                    select={'timestamp': 'date'}
                ).annotate(
                    max_quantity=Max('quantity'), min_quantity=Min('quantity'), avg_quantity=Avg('quantity')
                ).filter(
                    timestamp__gte=start_date, timestamp__lte=end_date, shop__icontains=shop, branch__icontains=branch,
                    product__icontains=product)

            elif interval == 'monthly':
                queryset = queryset.annotate(
                    date=TruncMonth('timestamp', tzinfo=pytz.UTC)
                ).values(
                    'date'
                ).extra(
                    select={'timestamp': 'date'}
                ).annotate(
                    max_quantity=Max('quantity'), min_quantity=Min('quantity'), avg_quantity=Avg('quantity')
                ).filter(
                    timestamp__gte=start_date, timestamp__lte=end_date, shop__icontains=shop, branch__icontains=branch,
                    product__icontains=product)

            elif interval == 'yearly':
                queryset = queryset.annotate(
                    date=TruncYear('timestamp', tzinfo=pytz.UTC)
                ).values(
                    'date'
                ).extra(
                    select={'timestamp': 'date'}
                ).annotate(
                    max_quantity=Max('quantity'), min_quantity=Min('quantity'), avg_quantity=Avg('quantity')
                ).filter(
                    timestamp__gte=start_date, timestamp__lte=end_date, shop__icontains=shop, branch__icontains=branch,
                    product__icontains=product)
        else:
            queryset = queryset

        return queryset

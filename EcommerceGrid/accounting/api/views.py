from accounting.models import *
from accounting.api.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import mixins
from django.db.models import Sum
import pytz
from django.db.models.functions import TruncMonth, TruncYear, TruncDate


class TransactionGraphListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TransactionGraphSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Transaction.objects.all()

    def get_queryset(self):
        queryset = super(TransactionGraphListViewSet, self).get_queryset()

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        interval = self.request.query_params.get('interval')
        transaction_type = self.request.query_params.get('transaction_type')

        if interval == 'daily':
            queryset = queryset.annotate(
                date=TruncDate('date_time', tzinfo=pytz.UTC)
            ).values(
                'date'
            ).extra(
                select={'date_time': 'date'}
            ).annotate(
                total=Sum(transaction_type)
            ).filter(
                date_time__gte=start_date, date_time__lte=end_date)

        elif interval == 'monthly':
            queryset = queryset.annotate(
                date=TruncMonth('date_time', tzinfo=pytz.UTC)
            ).values(
                'date'
            ).extra(
                select={'date_time': 'date'}
            ).annotate(
                total=Sum(transaction_type)
            ).filter(
                date_time__gte=start_date, date_time__lte=end_date)

        elif interval == 'yearly':
            queryset = queryset.annotate(
                date=TruncYear('date_time', tzinfo=pytz.UTC)
            ).values(
                'date'
            ).extra(
                select={'date_time': 'date'}
            ).annotate(
                total=Sum(transaction_type)
            ).filter(
                date_time__gte=start_date, date_time__lte=end_date)

        return queryset

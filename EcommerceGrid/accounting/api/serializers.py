from rest_framework import serializers
from accounting.models import *


class TransactionGraphSerializer(serializers.ModelSerializer):
    date = serializers.CharField()
    total = serializers.FloatField()

    class Meta:
        model = Transaction
        fields = ['date', 'total']

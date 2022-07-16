from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# class BookSummarySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['title', 'ratings']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True, many=True)
    # books = BookSummarySerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = '__all__'

from rest_framework import serializers
from .models import Book, User, Order


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

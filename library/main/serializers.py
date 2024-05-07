from rest_framework import serializers

from main.models import Book, Order


class BookSerializer(serializers.ModelSerializer):
    # реализуйте сериализацию объектов модели Book
    class Meta:
        model = Book
        fields = ["id", "author", "title", "year"]

    def delete(self, instance, validated_data):
        print(validated_data)
        return super().update(validated_data)

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['orders_count'] = ...
    #     return representation


class OrderSerializer(serializers.ModelSerializer):
    # добавьте поля модели Order
    class Meta:
        model = Order
        fields = ["id", "user_name", "days_count", "date", "books"]

    #доп задание
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['books'] = ...
    #     return representation

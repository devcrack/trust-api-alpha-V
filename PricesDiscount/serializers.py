from rest_framework import serializers
#
from .models import Discount, Credit, Price


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Price
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.tax_percentage = validated_data.get('tax_percentage', instance.tax_percentage)
        instance.Price_Description = validated_data.get('Price_Description', instance.Price_Description)
        instance.save()
        return instance


class CreditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credit
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.discount_percentage = validated_data.get('discount_percentage', instance.discount_percentage)
        instance.discount_price = validated_data.get('discount_price', instance.discount_price)
        instance.Discount_Description = validated_data.get('Discount_Description', instance.Discount_Description)
        instance.save()
        return instance




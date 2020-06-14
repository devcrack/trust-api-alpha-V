from rest_framework import serializers
#
from .models import ServiceArea
from PricesDiscount.models import Price, Discount
from PricesDiscount.serializers import PriceSerializer, DiscountSerializer


class ServiceAreaSerializerWrite(serializers.ModelSerializer):
    price = PriceSerializer(many=False)
    discount = DiscountSerializer(many=False)

    class Meta:
        model = ServiceArea
        fields = ['id', 'gas_company', 'name', 'price', 'discount']

    # def create(self, validated_data):

    def create(self, validated_data):
        price_data = validated_data.pop('price')
        discount_data = validated_data.pop('discount')
        _price = Price.objects.create(**price_data)
        _discount = Discount.objects.create(**discount_data)
        validated_data.update(price=_price)
        validated_data.update(discount=_discount)
        return ServiceArea.objects.create(**validated_data)

    def update(self, instance, validated_data):
        price_data = validated_data.get('price')
        discount_data = validated_data.get('discount')
        serializer_price = PriceSerializer(data=price_data, partial=True)
        if serializer_price.is_valid(raise_exception=True):
            validated_data['price'] = serializer_price.update(instance=instance.price, validated_data=price_data)
            serializer_discount = DiscountSerializer(data=discount_data, partial=True)
            if serializer_discount.is_valid(raise_exception=True):
                validated_data['discount'] = serializer_discount.update(validated_data=discount_data,
                                                                        instance=instance.discount)
                instance.price = validated_data.get('price', instance.price)
                instance.discount = validated_data.get('discount', instance.discount)
                instance.gas_company = validated_data.get('gas_company', instance.gas_company)
                instance.name = validated_data.get('name', instance.name)
                instance.save()
                return instance





from rest_framework import serializers
#
from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.street = validated_data.get('street', instance.street)
        instance.neighborhood = validated_data.get('neighborhood', instance.neighborhood)
        instance.inner_number = validated_data.get('inner_number', instance.inner_number)
        instance.outer_number = validated_data.get('outer_number', instance.outer_number)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.municipality = validated_data.get('municipality', instance.municipality)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()
        return instance



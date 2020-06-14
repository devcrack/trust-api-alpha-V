from rest_framework import serializers
from django.contrib.auth.models import Group
#
from .models import GasCompanyUser, GasCompany
from User.serializers import UserSerializer
from Addresses.serializer import AddressSerializer
from Addresses.models import Address
from User.models import User


class GasCompanySerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = GasCompany
        fields = '__all__'

    def create(self, validated_data):
        """
        The `.create()` method does not support writable nested fields by default.
        Write an explicit `.create()` method for serializer `GasCompany.serializer.GasCompanySerializer`,
        or set `read_only=True` on nested serializer fields.
        """
        address_data = validated_data.pop('address')
        addrs = Address.objects.create(**address_data)
        validated_data.update(address=addrs)
        return GasCompany.objects.create(**validated_data)

    def update(self, instance, validated_data):
        data_address = validated_data.get('address')
        address_serializer = AddressSerializer(data=data_address, partial=True)
        if address_serializer.is_valid(raise_exception=True):
            _address = address_serializer.update(instance=instance.address, validated_data=address_serializer.validated_data)
            # _address.save()
            validated_data['address'] = _address
            instance.name = validated_data.get('name', instance.name)
            instance.address = validated_data.get('address', instance.address)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.save()
        return instance


class UserCompanyWriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    gas_company = serializers.PrimaryKeyRelatedField(required=False, queryset=GasCompany.objects.all())
    type_user = serializers.CharField(max_length=3, write_only=True)

    class Meta:
        model = GasCompanyUser
        fields = ['id', 'user', 'gas_company', 'type_user']

    def create(self, validated_data):
        _user = self.context['user']
        try:
            gas_station_admin = GasCompanyUser.objects.get(user=_user)
            gas_station = gas_station_admin.gas_company
            validated_data.update(gas_company=gas_station)
        except GasCompanyUser.DoesNotExist:
            try:
                validated_data['gas_company']
            except KeyError:
                raise serializers.ValidationError({"gas_company": "Este campo es Requerido"})

        user_data = validated_data.pop('user')
        raw_password = user_data.pop('password')
        user_instance = User.objects.create(**user_data)
        user_instance.set_password(raw_password)
        user_instance.save()
        type_user = validated_data.pop('type_user')
        if type_user == '40C':  # AdminGasCompany
            try:
                user_group = Group.objects.get(name='AdminGasCompany')
            except Group.DoesNotExist:
                raise serializers.ValidationError('El grupo AdminGasCompany No existe')
            user_group.user_set.add(user_instance)
        elif type_user == '20C':
            try:
                user_group = Group.objects.get(name='Employee')
            except Group.DoesNotExist:
                raise serializers.ValidationError('El grupo Employee No existe')
            user_group.user_set.add(user_instance)
        elif type_user == 'ED':
            try:
                user_group = Group.objects.get(name='Operator')
            except Group.DoesNotExist:
                raise serializers.ValidationError('El grupo Operator No existe')
            user_group.user_set.add(user_instance)

        validated_data.update(user=user_instance)
        g_user = GasCompanyUser.objects.create(**validated_data)
        return g_user

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')
        user_serializer = UserSerializer(data=user_data, partial=True)  # Parcial=True, para evitarnos la validacion de los campos que son requeridos ya que podriamos solo querer actualizar ciertos campos de la instancia
        if user_serializer.is_valid(raise_exception=True):
            user_instance = user_serializer.update(instance=instance.user, validated_data=user_serializer.validated_data)

            validated_data['user'] = user_instance
            instance.user = validated_data.get('user', instance.user)
            instance.gas_company = validated_data.get('gas_company', instance.gas_company)
            instance.save()
            return instance






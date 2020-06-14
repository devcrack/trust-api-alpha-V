from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import phonenumbers
from phonenumbers import NumberParseException
from rest_framework.serializers import Serializer
from django.contrib.auth.models import Group
from rest_framework.utils import serializer_helpers
#
from .models import User
from Trust.Utils.phone_number import number_phone_is_not_valid
from GasCompany.models import GasCompanyUser


class UserRetrieveDataSerializer(serializers.ModelSerializer):
    role = serializers.IntegerField(read_only=True)
    gas_company = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'role', 'cellNumber1', 'cellNumber2', 'gas_company']
        read_only_fields = fields

    @property
    def data(self):
        returned_dictionary = super(Serializer, self).data
        _user = User.objects.get(pk=returned_dictionary['id'])
        returned_dictionary['gas_company'] = None

        if _user.is_staff:
            returned_dictionary['role'] = 0
        elif not _user.groups.all().count():
            returned_dictionary['role'] = -1
        else:

            if _user.groups.get() == Group.objects.get(name='AdminGasCompany'):
                returned_dictionary['role'] = 1
            elif _user.groups.get() == Group.objects.get(name='Employee'):
                returned_dictionary['role'] = 2
            elif _user.groups.get() == Group.objects.get(name='Operator'):
                returned_dictionary['role'] = 3
            gas_company_user = GasCompanyUser.objects.get(user=_user)
            returned_dictionary['gas_company'] = gas_company_user.gas_company.pk
        return serializer_helpers.ReturnDict(returned_dictionary, serializer=self)



class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    first_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    last_name = serializers.CharField(required=True, allow_null=False, allow_blank=False)
    email = serializers.EmailField(required=False, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=False, write_only=True) #El campo no es requerido mas sin embargo en la creacion siempre le pasamos un password, en cambio en el update este puede ir o no.
    cellNumber1 = serializers.CharField(allow_blank=False, validators=[UniqueValidator(queryset=User.objects.all())],
                                        min_length=13, max_length=16)
    cellNumber2 = serializers.CharField(required=False, validators=[UniqueValidator(queryset=User.objects.all())],
                                        min_length=13, max_length=16)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'username', 'cellNumber1', 'cellNumber2']

    def validate(self, data):
        if 'cellNumber1' in data:
            number_to_parse = data['cellNumber1']
            is_invalid = number_phone_is_not_valid(number_to_parse)
            if is_invalid:
                raise serializers.ValidationError(is_invalid)
        if 'cellNumber2' in data:
            number_to_parse = data['cellNumber2']
            is_invalid = number_phone_is_not_valid(number_to_parse)
            if is_invalid:
                raise serializers.ValidationError(is_invalid)
        return data

    def create(self, validated_data):
        raw_password = validated_data.pop('password')
        user_instance = User.objects.create(**validated_data)
        user_instance.set_password(raw_password)
        user_instance.save()
        return user_instance

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.cellNumber1 = validated_data.get('cellNumber1', instance.cellNumber1)
        instance.cellNumber2 = validated_data.get('cellNumber2', instance.cellNumber2)
        if 'password' in validated_data:
            raw_password = validated_data.pop('password')
            instance.set_password(raw_password)
        instance.save()
        return instance





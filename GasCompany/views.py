from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from knox.views import Response
from rest_framework import status
# Create your views here.
from .models import GasCompany, GasCompanyUser
from .serializer import GasCompanySerializer, UserCompanyWriteSerializer
from Trust.Authentication.permissions import HasGroupPermissions

class AdministratorGasStationView(ModelViewSet):
    permission_classes = [IsAdminUser]


class GasCompanyView(ModelViewSet):
    """
    View to do CRUD of this resource(GasCompany model)
    """
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = GasCompany.objects.all()
    serializer_class = GasCompanySerializer


class GasCompanyAdminView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserCompanyWriteSerializer

    def get_queryset(self):
        return GasCompanyUser.objects.filter(user__groups__name='AdminGasCompany')

    def create(self, request, *args, **kwargs):
        request.data.update(type_user='40C')
        _serializer = UserCompanyWriteSerializer(data=request.data, context={'user': request.user})
        if _serializer.is_valid(raise_exception=True):
            _serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=_serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_attached = instance.user
        user_attached.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GasCompanyEmployeeView(ModelViewSet):
    required_groups = {
        'GET': ['AdminGasCompany'],
        'POST': ['AdminGasCompany'],
        'PATCH': ['AdminGasCompany'],
        'DELETE': ['AdminGasCompany']
    }
    permission_classes = [IsAuthenticated, IsAdminUser | HasGroupPermissions]
    serializer_class = UserCompanyWriteSerializer

    def get_queryset(self):
        _user = self.request.user
        if _user.is_staff:
            _query_set = GasCompanyUser.objects.all()
        else:
            try:
                gas_company_user = GasCompanyUser.objects.get(user=_user)
            except GasCompanyUser.DoesNotExist:
                return None
            _query_set = GasCompanyUser.objects.filter(gas_company=gas_company_user.gas_company)
            _query_set = _query_set.filter(user__groups__name='Employee')
            _query_set = _query_set.exclude(user=_user)
            return _query_set

    def create(self, request, *args, **kwargs):
        request.data.update(type_user='20C')

        _serializer = UserCompanyWriteSerializer(data=request.data, context={'user': request.user})
        if _serializer.is_valid(raise_exception=True):
            _serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=_serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        user_attached = instance.user
        user_attached.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

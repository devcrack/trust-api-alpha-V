from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from knox.views import Response
from rest_framework import status
#
from .serializers import ServiceAreaSerializerWrite
from Trust.Authentication.permissions import HasGroupPermissions
from .models import ServiceArea
from GasCompany.models import GasCompanyUser


class ServiceAreaview(ModelViewSet):
    required_groups = {
        'GET': ['AdminGasCompany'],
        'POST': ['AdminGasCompany'],
        'PATCH': ['AdminGasCompany'],
        'DELETE': ['AdminGasCompany']
    }
    permission_classes = [IsAuthenticated, IsAdminUser | HasGroupPermissions]
    serializer_class = ServiceAreaSerializerWrite
    # queryset = ServiceArea.objects.all()

    def get_queryset(self):
        _user = self.request.user
        if _user.is_staff:
            return ServiceArea.objects.all()
        else:
            try:
                gas_company_user = GasCompanyUser.objects.get(user=_user)
            except GasCompanyUser.DoesNotExist:
                return None
            return ServiceArea.objects.filter(gas_company=gas_company_user.gas_company)


    def destroy(self, request, *args, **kwargs):
        instance_to_destroy = self.get_object()
        price_attached = instance_to_destroy.price
        price_attached.delete()
        discount_attached = instance_to_destroy.discount
        discount_attached.delete()
        instance_to_destroy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


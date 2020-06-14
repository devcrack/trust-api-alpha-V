from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
# from User.models import User
from User.models import RawToken


class LoginView(KnoxLoginView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data) # Aqui si usamos el nombre de usuario para iniciar sesion
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        data_to_response = super(LoginView, self).post(request, format=None)
        _token = data_to_response.data['token']
        RawToken.objects.create(user=user, token=_token)
        return data_to_response

from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from knox.views import APIView, Response
# Create your views here.
from .models import User
from .serializers import UserRetrieveDataSerializer


class UsersMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        user = User.objects.get(pk=self.request.user.pk)
        _serializer = UserRetrieveDataSerializer(user, many=False)
        return Response(data=_serializer.data)

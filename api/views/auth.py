from ..serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
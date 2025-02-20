from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegistrationSerializer, UserSerializer, LoginSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes= (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
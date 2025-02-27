from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers.authenticationserializer import AuthenticationSerializer

class AuthenticationView(TokenObtainPairView):
    """
    This view is used to validate otp and generate jwt token
    """
    serializer_class = AuthenticationSerializer
    permission_classes = [AllowAny] # Bypass JWT for /create API
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
"""
View for User model
"""

from rest_framework import generics
from user.serializers.userserializer import UserSerializer
from user.serializers.otpserializer import OTPSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers.authenticationserializer import AuthenticationSerializer
from user.models import User, UserRole

class CreateUserView(generics.CreateAPIView):
    """
    This view is used to create user
    """
    permission_classes = [AllowAny] # Bypass JWT for /create API
    serializer_class = UserSerializer # Uses User serializer to create user in the system

class UserView(generics.CreateAPIView):
    """
    This view is used to update user details
    """
    serializer_class = UserSerializer # Uses User serializer to update user in the system

    def get(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
   
   

    def put(self, request):
        """
         This methode updates the role of user
        """
        user = self.get(request.data.get("email"))

        if user is None:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # User at a lower level can't update the role of user at higher level
        # User at a level can assign roles less than their role
        if request.data.get('role_id') >= request.user.role_id.id or user.role_id.id >= request.user.role_id.id :
            return Response({"error": "You are not authorized to update the role"}, status=status.HTTP_401_UNAUTHORIZED)
        
        userrole = UserRole.objects.get(id=request.data.get('role_id'))
        user.role_id = userrole

        user.save()
       
        return Response(status=status.HTTP_200_OK)
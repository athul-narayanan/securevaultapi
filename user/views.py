"""
View for User model
"""

from rest_framework import generics
from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """
    This view is used to create user
    """
    serializer_class = UserSerializer # Uses User serializer to create user in the system
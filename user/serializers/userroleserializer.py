from rest_framework import serializers
from user.models import UserRole


   
class UserRoleSerializer(serializers.ModelSerializer):
    """
    Serializer for Authentication.
    """

    class Meta:
        model = UserRole
        fields = "__all__"


from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
     Serializer to manage user objects
    """
    class Meta:
        model = get_user_model()
        fields = ["id","email", "mobile", "role_id", "firstname", "lastname", "password"]

    def create(self, data):
        """
        create and return a user
        """
        user = get_user_model().objects.create_user(**data)
        return {
            "id": user.id,
            "email": user.email,
            "mobile": user.mobile,
            "role_id": user.role_id,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "password": "*****************"
        }

class UserGetSerializer(serializers.ModelSerializer):
    """
     Serializer to manage user objects
    """
    class Meta:
        model = get_user_model()
        fields = ["id","email", "mobile", "role_id", "firstname", "lastname"]
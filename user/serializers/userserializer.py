

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
        return get_user_model().objects.create_user(**data)

class UserGetSerializer(serializers.ModelSerializer):
    """
     Serializer to manage user objects
    """
    class Meta:
        model = get_user_model()
        fields = ["id","email", "mobile", "role_id", "firstname", "lastname"]
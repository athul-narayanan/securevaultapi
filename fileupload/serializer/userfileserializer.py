"""
    serializer to access files of a user
"""

from rest_framework import serializers
from fileupload.models import UserFileAccess

class UserFileSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = UserFileAccess
        fields = '__all__'
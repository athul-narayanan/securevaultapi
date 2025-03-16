"""
    serializer to access files of a user
"""

from rest_framework import serializers
from fileupload.models import Files

class UserFileSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Files
        fields = '__all__'
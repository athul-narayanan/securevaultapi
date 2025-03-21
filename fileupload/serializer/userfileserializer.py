"""
    serializer to access files of a user
"""

from rest_framework import serializers
from fileupload.models import Files, UserFileAccess


class UserFileSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Files
        fields = ['id', 'file_link', 'file_name', 'created_time', 'size', 'type',  'user' ]

class SharedFileSerializer(serializers.ModelSerializer):
    """

    """
    
    file_name = serializers.CharField(source='file.file_name')
    file_link = serializers.CharField(source='file.file_link')
    type = serializers.CharField(source='file.type')
    size = serializers.CharField(source='file.size')

    class Meta:
        model = UserFileAccess
        fields = ['user','access','created_time', 'updated_time', 'file_name', 'file_link', 'type', 'size' ]
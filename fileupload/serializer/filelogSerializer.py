"""
    serializer for file log
"""

from rest_framework import serializers
from fileupload.models import UserFileLog

class FileLogSerializer(serializers.ModelSerializer):
    """
       Serializer to manage file logs 
    """
    file_name = serializers.CharField(source='file.file_name')
    file_link = serializers.CharField(source='file.file_link')
    type = serializers.CharField(source='file.type')
    size = serializers.CharField(source='file.size')
    user = serializers.CharField(source = 'user.email')

    class Meta:
        model = UserFileLog
        fields = ["message", "action", "file_name", "file_link", "type", "size", "user", "created_time"]
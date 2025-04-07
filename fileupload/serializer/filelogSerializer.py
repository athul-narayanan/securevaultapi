"""
    serializer for file log
"""

from rest_framework import serializers
from fileupload.models import UserFileLog

class FileLogSerializer(serializers.ModelSerializer):
    """
       Serializer to manage file logs 
    """

    class Meta:
        model = UserFileLog
        fields = '__all__'
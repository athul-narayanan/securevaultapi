from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from django.conf import settings
import os
import time
from utils.encrypt import decrypt_file
from fileupload.models import Files
from rest_framework import status



class FileHandleView(generics.GenericAPIView):
    """
    This view is used to download and delete file
    """
    
    def get(self, request, file_name):
       filepath = os.path.join(settings.MEDIA_ROOT, file_name )
       file_content = decrypt_file(filepath)
       
       response = HttpResponse(file_content, content_type='application/octet-stream')
       response['Content-Disposition'] = f'attachment; filename="{file_name}"'
       return response
    
    def delete(self, request, file_name):
        filepath = os.path.join(settings.MEDIA_ROOT, file_name )
        instance = Files.objects.get(file_link=file_name)
        print(filepath)
        if instance.user != request.user:
            return Response({"error": "you are not authorized to delete the file"}, status=status.HTTP_401_UNAUTHORIZED)
        if os.path.exists(filepath): 
            os.remove(filepath)
            instance.delete()
            return Response({"message":"File Deleted Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "file not found"}, status=status.HTTP_400_BAD_REQUEST)
    
            

            
        
            

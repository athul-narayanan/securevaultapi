from rest_framework import generics
from django.http import HttpResponse
from django.conf import settings
import os
import time
from utils.encrypt import decrypt_file


class FileDownloadView(generics.GenericAPIView):
    """
    This view is used to download file
    """
    
    def get(self, request, file_name):
       filepath = os.path.join(settings.MEDIA_ROOT, file_name )
       file_content = decrypt_file(filepath)
       
       response = HttpResponse(file_content, content_type='application/octet-stream')
       response['Content-Disposition'] = f'attachment; filename="{file_name}"'
       return response
            

            
        
            

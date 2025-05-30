from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
from django.conf import settings
import os
import time
from utils.encrypt import decrypt_file
from fileupload.models import Files, UserFileLog
from rest_framework import status
from auditlog.models import LogEntry
from django.contrib.contenttypes.models import ContentType



class FileHandleView(generics.GenericAPIView):
    """
    This view is used to download and delete file
    """
    def get(self, request, file_name):
       filepath = os.path.join(settings.MEDIA_ROOT, file_name )
       file_content = decrypt_file(filepath)
       # Create Audit log for file download
       LogEntry.objects.create(
            content_type=ContentType.objects.get_for_model(Files),
            action=3, 
            object_repr = file_name,
            changes_text = f"{file_name} downloaded",
            actor = request.user
        )
       
       file = Files.objects.get(file_link = file_name)
       # Add file access log entry
       UserFileLog.objects.create(
           action = "ACCESS",
           file_name = file.file_name,
           file_link = file.file_link,
           size = file.size,
           type = file.type,
           message = f"downloaded the file",
           user = request.user
       )
       response = HttpResponse(file_content, content_type='application/octet-stream')
       response['Content-Disposition'] = f'attachment; filename="{file_name}"'
       return response
    
    def delete(self, request, file_name):
        try:
            filepath = os.path.join(settings.MEDIA_ROOT, file_name )
            instance = Files.objects.get(file_link=file_name)
            if instance.user != request.user:
                return Response({"error": "you are not authorized to delete the file"}, status=status.HTTP_401_UNAUTHORIZED)
            if os.path.exists(filepath): 
                os.remove(filepath)
                UserFileLog.objects.create(
                    action = "DELETE",
                    message = f"deleted the file {file_name}",
                    file_name = instance.file_name,
                    file_link = instance.file_link,
                    size = instance.size,
                    type = instance.type,
                    user = request.user
                )
                instance.delete()
                return Response({"message":"File Deleted Successfully"}, status=status.HTTP_200_OK)
                
            else:
                return Response({"error": "file not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Files.DoesNotExist:
            return Response({"error": "file not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as expr:
            print(expr)
            return Response({"error": "invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    
            

            
        
            

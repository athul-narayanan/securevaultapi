from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from rest_framework import parsers
import os
import time
from utils.encrypt import encrypt_file
from fileupload.serializer.fileuploadserializer import FileUploadSerializer
from fileupload.models import Files
import magic

class FileUploadView(generics.GenericAPIView):
    """
    This view is used to upload file
    """

    serializer_class = FileUploadSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    def get_filesize(self,size_in_bytes):
        kb = 1024
        mb = kb* 1024

        if size_in_bytes < kb:
            return f"{size_in_bytes} bytes"
        elif size_in_bytes < mb:
            return f"{round(size_in_bytes/kb, 2)} KB"
        else:
            return f"{round(size_in_bytes/mb, 2)} MB"
        
    def get_filetype(self, file):
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(file.read(1024))
        file.seek(0) # reset the file pointer
        file_type = mime_type.split("/")[1].upper()
        return file_type


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            random_str = str(time.time())
            file = serializer.validated_data
            filesize = self.get_filesize(file['file'].size)
            filetype = self.get_filetype(file['file'])
            print(filesize, filetype)
            filepath = os.path.join(settings.MEDIA_ROOT, random_str + file["file"].name )
            with open(filepath, 'wb+') as f:
                data = file.get("file").read()
                iv, encypted_data = encrypt_file(data) # encrypt file before uploading
                f.write(iv)
                f.write(encypted_data)

            filename = file['file'].name
            filelink = f"{random_str}{file['file'].name}"

            updatedfile = Files.objects.create(
                file_name = filename,
                file_link = filelink,
                size = filesize,
                type=filetype,
                user = request.user
            )
            
            return Response({
                'message': 'File uploaded successfully',
                'id': updatedfile.id
            }, status=status.HTTP_200_OK)

        return Response("Upload a file to proceed", status=status.HTTP_400_BAD_REQUEST)
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from fileupload.models import Files
from django.conf import settings
from rest_framework import parsers
import os
import time
from utils.encrypt import encrypt_file
from fileupload.serializer.fileuploadserializer import FileUploadSerializer

class FileUploadView(generics.GenericAPIView):
    """
    This view is used to upload file
    """

    serializer_class = FileUploadSerializer
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            random_str = str(time.time())
            file = serializer.validated_data
            filepath = os.path.join(settings.MEDIA_ROOT, random_str + file["file"].name )
            with open(filepath, 'wb+') as f:
                data = file.get("file").read()
                iv, encypted_data = encrypt_file(data) # encrypt file before uploading
                f.write(iv)
                f.write(encypted_data)

            updatedfile = Files.objects.create(
                file_name = file['file'].name,
                file_link = f"{random_str}{file['file'].name}"
            )
            return Response({
                'message': 'File uploaded successfully',
                'id': updatedfile.id
            }, status=status.HTTP_200_OK)

        return Response("Upload a file to proceed", status=status.HTTP_400_BAD_REQUEST)
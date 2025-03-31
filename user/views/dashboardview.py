from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from fileupload.models import Files, UserFileAccess
from fileupload.serializer.userfileserializer import UserFileSerializer, SharedFileSerializer
from fileupload.serializer.filelogSerializer import FileLogSerializer
from fileupload.models import UserFileLog
from collections import Counter

class DashboardView(generics.GenericAPIView):
    def findtotal_size(self, files):
        total_size = 0
        for file in files:
            print(file["size"])
            splits  = file["size"].split(" ")
            print(splits)
            size = float(splits[0])
            type = splits[1]
            print(size, type)
            if type == "bytes":
                total_size += size/(1024*1024)
            elif type == "KB":
                total_size += size/1024
            else:
                total_size+=size
        return f"{round(total_size,4)} MB"

    def get(self, request):
        try:
            """
                This view is used to get dashboard of the user
            """
            # Find the number of files of the user
            files =  Files.objects.filter(user=request.user, is_delete=False)
            serializedData = UserFileSerializer(files, many=True)
            filecount = len(serializedData.data)
             # Find the count of each files
            file_types = [file['type'] for file in serializedData.data]
            file_type_counts = [{'type': type, 'count': count} for type, count in Counter(file_types).items()]
            
            file_size = self.findtotal_size(serializedData.data)
            print(file_size)

            # Find the number of files in the bin
            binfiles = Files.objects.filter(user=request.user, is_delete=True)
            serializedData = UserFileSerializer(binfiles, many=True)
            binfile_count = len(serializedData.data)

            # find the number of files shared with the user
            files =  UserFileAccess.objects.filter(user=request.user)
            serializedData = SharedFileSerializer(files, many=True)
            shared_count = len(serializedData.data)

            file_logs = UserFileLog.objects.filter(user = request.user)
            recent_logs = FileLogSerializer(file_logs, many=True)
            print(recent_logs.data)

            return Response( {
                'file': filecount,
                'total_size': file_size,
                'bin': binfile_count,
                'shared_count': shared_count,
                'files': file_type_counts,
                'recent_logs': recent_logs.data
            }, status=status.HTTP_200_OK)
        except Exception:
            Response({'error': "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

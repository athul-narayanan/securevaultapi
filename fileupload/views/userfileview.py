from rest_framework import generics
from rest_framework.response import Response
from fileupload.models import UserFileAccess
from fileupload.serializer.userfileserializer import UserFileSerializer

class UserFileView(generics.GenericAPIView):
    """
    This view is used to fetch and insert files associated with a user
    """

    def get(self, request):
        """
            Fetch all files accessible to the user
        """
        files =  UserFileAccess.objects.filter(user=request.user)
        serializedData = UserFileSerializer(files, many=True)
        return Response(serializedData.data)
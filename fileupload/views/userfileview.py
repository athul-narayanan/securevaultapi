from rest_framework import generics
from rest_framework.response import Response
from fileupload.models import Files, UserFileAccess
from fileupload.serializer.userfileserializer import UserFileSerializer, SharedFileSerializer
import os
from django.utils import timezone
from django.conf import settings
from rest_framework import status
from user.models import User
from fileupload.models import FileAccessRoles

class UserFileView(generics.GenericAPIView):
    """
    This view is used to fetch files owned by the user
    """

    def get(self, request):
        """
            Fetch all files accessible to the user
        """
        files =  Files.objects.filter(user=request.user,is_delete=False)
        serializedData = UserFileSerializer(files, many=True)
        return Response(serializedData.data)

class ShareFileView(generics.GenericAPIView):
    """
    This view is to assign file access to users and get shared files
    """

    def get(self, request):
        files = UserFileAccess.objects.filter(user=request.user)
        serializedData = SharedFileSerializer(files, many=True)
        return Response(serializedData.data)
    
    def delete(self, request):
        if request.query_params.get('id') is None:
            return Response(
                {
                    "error": f"Invalid request"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        id = int(request.query_params.get('id'))
        try:
            files = UserFileAccess.objects.filter(user=request.user, file=id)
            if not files.exists():
                raise  UserFileAccess.DoesNotExist
            files.delete()
            return Response({"message": "file deleted successfully"}, status=status.HTTP_200_OK)
        except UserFileAccess.DoesNotExist:
            return Response(
                {
                    "error": f"File does not exist"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except:
            return Response(
                {
                    "error": f"Failed to delete file"
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def post(self, request):
        file_id = request.data.get("id")
        users = request.data.get("users")
        try:
            file = Files.objects.get(id=file_id, is_delete=False)
            for user in users:
                try:
                    user_id = user.get("user_id")
                    access_id = user.get("access_id")
                    user_data = User.objects.get(id = user_id)
                    access = FileAccessRoles.objects.get(id=access_id)
                    file_access, created = UserFileAccess.objects.update_or_create(
                        file= file,
                        user=user_data,
                        defaults={
                            'file': file,
                            'user': user_data,
                            'access': access,
                            "updated_time": timezone.now()
                        }
                    )

                    if created :
                        pass
                    else:
                        pass
                except User.DoesNotExist:
                    return Response(
                        {
                            "error": f"User does not exist for {user.user_id}"
                        }, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
                except FileAccessRoles.DoesNotExist:
                    return Response(
                        {
                            "error": f"Access does not exist for user id = {user.user_id} and acess id={user.access_id}"
                        }, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
        except Files.DoesNotExist:
            return Response({"error": "File does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "Invalid Request"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"messge": "User access updated successfully"}, status=status.HTTP_200_OK)


class MoveToBinView(generics.GenericAPIView):
    """
    This view is to move files to bin
    """

    def delete(self, request, file_name):
        try:
            filepath = os.path.join(settings.MEDIA_ROOT, file_name )
            instance = Files.objects.get(file_link=file_name)
    
            if instance.user != request.user:
                return Response({"error": "you are not authorized to move the file to bin"}, status=status.HTTP_401_UNAUTHORIZED)
            if os.path.exists(filepath): 
                instance.is_delete = True
                instance.save()
                return Response({"message":"File Moved to Bin Successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "file not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Files.DoesNotExist:
            return Response({"error": "file not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, file_name):
        """
            Restore files in bin
        """
        try:

            filepath = os.path.join(settings.MEDIA_ROOT, file_name )
            instance = Files.objects.get(file_link=file_name, is_delete=True)
        
            if instance.user != request.user:
                return Response({"error": "you are not authorized to restore the file from bin"}, status=status.HTTP_401_UNAUTHORIZED)
            if os.path.exists(filepath): 
                instance.is_delete = False
                instance.save()
                return Response({"message":"File restored from bin successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "File not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Files.DoesNotExist:
            return Response({"error": "file not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "invalid request"}, status=status.HTTP_400_BAD_REQUEST)
    
class BinFileView(generics.GenericAPIView):
    """
    This view is to get files in bin
    """

    def get(self,request):
        """
            Fetch all files in bin
        """
        files =  Files.objects.filter(user=request.user,is_delete=True)
        serializedData = UserFileSerializer(files, many=True)
        return Response(serializedData.data)

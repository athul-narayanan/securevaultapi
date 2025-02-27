from rest_framework import generics
from rest_framework.response import Response
from user.serializers.userroleserializer import UserRoleSerializer
from user.models import UserRole


class UserRolesView(generics.ListAPIView):
    """
    This view is used to fetch all user roles
    """
    serializer_class = UserRoleSerializer
    
    def get(self, request):
        userroles = UserRole.objects.all()
        serializedData = UserRoleSerializer(userroles, many=True)
        return Response(serializedData.data)
    
class UserRoleItemView(generics.GenericAPIView):
    """
    This view is used to fetch user role by id
    """

    def get(self, request, role_id):
        userrole = UserRole.objects.get(id=role_id)
        serializedData = UserRoleSerializer(userrole)
        return Response(serializedData.data)
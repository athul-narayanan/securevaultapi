from rest_framework import generics
from rest_framework import status
from auditlog.models import LogEntry
from auditlogs.serializer.AuditLogSerializer import AuditLogSerializer
from rest_framework.response import Response

class AuditLogView(generics.GenericAPIView):
    serializer_class = AuditLogSerializer

    def get(self, request):
        try:
            if request.user.role_id.role_name == "MASTER":
                logs = LogEntry.objects.all()
                serialized_data = AuditLogSerializer(logs, many=True)
                print(serialized_data)
                return Response(serialized_data.data)
            else:
                return Response(
                    {"message":"You are not authorized to access audit logs"}, 
                    status=status.HTTP_200_OK
                )
        except Exception as expr:
            print(expr)
            return Response(
                    {"message":"invalid request"}, 
                    status=status.HTTP_400_BAD_REQUEST
            )
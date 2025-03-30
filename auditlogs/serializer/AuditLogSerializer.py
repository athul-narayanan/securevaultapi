from auditlog.models import LogEntry

"""
    serializer to access Audit logs
"""


from rest_framework import serializers

class AuditLogSerializer(serializers.ModelSerializer):
    actor = serializers.SerializerMethodField()
    action = serializers.SerializerMethodField()
    content_type = serializers.SerializerMethodField()
    class Meta:
        model = LogEntry
        fields = "__all__"

    def get_actor(self, obj):
        return obj.actor.email if obj.actor else None
    
    def get_action(self, obj):
        action_map = {
            0: "CREATED",
            1: "UPDATED",
            2: "DELETED",
            3: "VIEWED"
        }
        return action_map.get(obj.action, "UNKNOWN_ACTION")
    
    def get_content_type(self, obj):
        if obj.content_type:
            return f"{obj.content_type.model}"
        return None



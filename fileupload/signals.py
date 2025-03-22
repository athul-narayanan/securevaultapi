# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from auditlog.models import LogEntry
from fileupload.utils import get_current_user

@receiver(pre_save, sender=LogEntry)
def add_user_to_log_entry(sender, instance, **kwargs):
    """Add current user in audit log entry"""
    user = get_current_user()
    if user and user.is_authenticated:
        instance.actor = user
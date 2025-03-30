"""
defines url mapping for the audit log API
"""

from django.urls import path
from auditlogs.views.AuditLogView import AuditLogView

urlpatterns = [
    path('', AuditLogView.as_view()) 
]
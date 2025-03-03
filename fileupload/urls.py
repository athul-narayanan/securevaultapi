"""
defines url mapping for the user API
"""

from django.urls import path
from fileupload.views.fileuploadview import FileUploadView
from  fileupload.views.filedownloadview import FileDownloadView



urlpatterns = [
    path('upload', FileUploadView.as_view()),
    path('upload/<str:file_name>', FileDownloadView.as_view())
]
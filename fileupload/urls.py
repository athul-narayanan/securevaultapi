"""
defines url mapping for the user API
"""

from django.urls import path
from fileupload.views.fileuploadview import FileUploadView
from  fileupload.views.filedownloadview import FileHandleView
from fileupload.views.userfileview import UserFileView, ShareFileView, MoveToBinView

urlpatterns = [
    path('upload', FileUploadView.as_view()),
    path('upload/<str:file_name>', FileHandleView.as_view()),
    path('files', UserFileView.as_view()),
    path('files/shared', ShareFileView.as_view()),
    path('files/bin/<str:file_name>', MoveToBinView.as_view()),
]
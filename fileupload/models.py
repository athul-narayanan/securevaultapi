from django.db import models

from user.models import User



class Files(models.Model):
    """
    This model defines files to be uploaded
    """

    class Meta:
        db_table = 'files'

    file_name = models.CharField(max_length=255)
    file_link = models.CharField(max_length=255, unique=True)
    created_time = models.DateField(auto_now=True)
    size = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

class FileAccessRoles(models.Model):
    """
    This model defines file access roles in the system
    """

    class Meta:
        db_table = 'fileaccessroles'

    role_name = models.CharField(max_length=255, unique=True)
    is_delete = models.BooleanField(default=False)
    is_view = models.BooleanField(default=True)
    is_download = models.BooleanField(default=False)

class UserFileAccess(models.Model):
    """
    This model defines uploaded files and access given to users
    """

    class Meta:
        db_table = 'userfileaccess'

    file = models.ForeignKey(Files, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.ForeignKey(FileAccessRoles, on_delete=models.CASCADE)
    created_time = models.DateField(auto_now=True)
    updated_time = models.DateField(auto_now=True)


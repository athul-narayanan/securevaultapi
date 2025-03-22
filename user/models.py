"""
This file contains database models
"""
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
)

from auditlog.registry import auditlog


class UserManager(BaseUserManager):
    """
    Manager class for User model
    """
    def create_user(self, email, password, **extrafields):
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password, **fields):
        """
            Creates super user
        """
        fields.setdefault("is_staff", "True")
        fields.setdefault("is_superuser", "True")

        return self.create_user(email, password, **fields)


class UserRole(models.Model):
    """
    This model defines user role in the system
    """

    class Meta:
        db_table = 'userrole'

    role_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.role_name

class User(AbstractBaseUser):
    """
    This model defines user in the system
    """
    class Meta:
        db_table = 'user' 
        
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=14)
    password = models.CharField(max_length=255)
    role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE, default=1)
    objects = UserManager()
    is_staff = models.BooleanField(default=False)  
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    
    def has_module_perms(self, app_label):
        """
            Return true if a user has access for given app
        """
        if self.is_superuser:
            return True
        return False

    def has_perm(self, perm, obj=None):
        """
           Return true if user has specific permission
        """
        if self.is_superuser:
            return True
        return False

auditlog.register(User)
auditlog.register(UserRole)
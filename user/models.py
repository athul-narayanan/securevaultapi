"""
This file contains database models
"""
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
)

class UserManager(BaseUserManager):
    """
    Manager class for User model
    """
    def create_user(self, email, password, **extrafields):
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save()

        return user


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
        
    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=14)
    password = models.CharField(max_length=255)
    role_id = models.ForeignKey(UserRole, on_delete=models.CASCADE, default=1)
    objects = UserManager()

    USERNAME_FIELD = 'email'

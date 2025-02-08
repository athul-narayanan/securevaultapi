"""
This file contains database models

"""
from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
)

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extrafields):
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save()

        return user

    

class User(AbstractBaseUser):
    """
    This model defines user in the system
    """
    class Meta:
        db_table = 'user'

    email = models.EmailField(max_length=255, unique=True)
    mobile = models.CharField(max_length=14)
    password = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'

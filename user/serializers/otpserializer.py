
from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
import pyotp
import pickle
from utils.cache import set_cache

class OTPSerializer(serializers.Serializer):
    """
    Serializer for OTP generation
    """

    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    
    def validate(self, data):
        """
        This method validates the user name and password using default
        autheticate method
        """
        email = data.get("email")
        password = data.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
           raise AuthenticationFailed("User name or password is wrong")
        
        otp = self.generare_otp()
        set_cache(otp,  pickle.dumps(user)) # serialize and store otp in cache
        self.send_mail(email, otp)

        return data
        
    def generare_otp(self):
        """
        This method generates otp
        """

        totp = pyotp.TOTP('base32secret3232')
        return totp.now()
    
    def send_mail(self, email, otp):
        send_mail(
        "One Time Password",
        f"Dear  Customer, {otp} is your OTP. It will expire in 600 Second(s). Do not share this OTP with anyone",
        "athulnarayanan62@gmail.com",
        [email],
        fail_silently=False,
        )

        
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
import pickle
from rest_framework.exceptions import AuthenticationFailed
from utils.cache import  get_cache


   
class AuthenticationSerializer(serializers.Serializer):
    """
    Serializer for Authentication.
    """

    email = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)
    

    def validate(cls, user):
        """
        This method verifies the otp and send JWT token
        """

        userdata =  get_cache(user['otp'])
    
        # if userdata is None or userdata["email"] != user["email"]:
        #    raise AuthenticationFailed("Invalid/Expired OTP")
        
        userdata = pickle.loads(userdata)

        refresh = RefreshToken.for_user(userdata)
        access_token = refresh.access_token

        return {
            'refresh': str(refresh),    
            'access': str(access_token),
            'email': userdata.email,
            'firstname': userdata.firstdata,
            'lastname' : userdata.lastname,
            'usertype': userdata.role_id.role_name
        }
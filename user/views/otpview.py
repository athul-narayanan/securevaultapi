from rest_framework import generics
from user.serializers.otpserializer import OTPSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
    

class GenerataOtpView(generics.CreateAPIView):
    """
    This view is used to generate otp
    """
    permission_classes = [AllowAny] # Bypass JWT for /generate/otp API
    serializer_class = OTPSerializer # Uses OTPSerializer to generate OTP

    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                'message': 'OTP sent successfully to your email.'
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
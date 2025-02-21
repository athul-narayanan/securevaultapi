"""
defines url mapping for the user API
"""

from django.urls import path
from user.views.authenticationview import AuthenticationView
from user.views.otpview import GenerataOtpView
from user.views.userview import CreateUserView


urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('otp/generate/', GenerataOtpView.as_view()),
    path('login/', AuthenticationView.as_view())
]
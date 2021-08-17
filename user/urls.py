from django.contrib.auth.models import User
from django.urls import path
from .views import UserMe, Register
from rest_framework_jwt.views  import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
urlpatterns = [
    path('me/',UserMe.as_view()),
    path('register/',Register.as_view()),
    path('api-jwt/', obtain_jwt_token),
    path('api-jwt-ref/', refresh_jwt_token),
    path('api-jwt-ver/',verify_jwt_token),
]
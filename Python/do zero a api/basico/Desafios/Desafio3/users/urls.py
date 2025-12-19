from django.urls import path
from .views import UserView, LoginJTWView
from rest_framework_simplejwt import views

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/login/', LoginJTWView.as_view())
]
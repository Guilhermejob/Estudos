from django.urls import path
from .views import MusicianView#, LoginJWTView
from rest_framework_simplejwt import views

urlpatterns = [
    path('musicians/', MusicianView.as_view()),
    path('token/', views.TokenObtainPairView.as_view()),
    path('token/refresh/', views.TokenRefreshView.as_view())
]
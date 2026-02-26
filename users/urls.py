from django.contrib.auth.views import PasswordChangeView
from django.urls import path
from .views import SignUpView, LoginView, LogoutView, ProfileView, ChangePasswordView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
]
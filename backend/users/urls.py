from django.urls import path
from .views import RegistrationView, LoginView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserDetailView.as_view(), name='user_detail')
]
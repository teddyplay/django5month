from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users.views import SignUp, SignIn


urlpatterns = [
    path('api/v1/sign/up/', SignUp.as_view({"post":"create"})),
    path('api/v1/sign/in/', SignIn.as_view(), name='jwt_create'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='verify'),
]

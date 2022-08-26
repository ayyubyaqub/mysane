from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('education_details', educationdetail, basename='educationdetail')
# urlpatterns1 = router.urls

urlpatterns=[
    path('register/',RegisterView.as_view()),
    path('verify-otp/',VerifyOtp.as_view()),
    path('Login/',LoginView.as_view()),
    path('education_details/',educationdetail.as_view()),
    path('education_details/<int:pk>',educationdetail.as_view()),
]
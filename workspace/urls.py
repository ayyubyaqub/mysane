from django.urls import path
from .views import *
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns=[
    path('workspace/',Work_space_view.as_view()),

]
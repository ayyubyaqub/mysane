from django.urls import path
from .views import *
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns=[
    path('workspace/',Work_space_view.as_view()),
    path('workspace/<int:pk>',Work_space_view.as_view()),
    path('project/',project_view.as_view()),
    path('project/<int:pk>',project_view.as_view()),
    path('task/',task_view.as_view()),
    path('task/<int:pk>',task_view.as_view()),

]
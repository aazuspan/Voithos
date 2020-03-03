from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('api/', views.api_response, name='api'),
]

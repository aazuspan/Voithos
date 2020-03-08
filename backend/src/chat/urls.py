from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_response, name='api'),
]

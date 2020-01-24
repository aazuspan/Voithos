from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('about', views.about, name='about'),
    path('docs', views.documentation, name='docs')
]

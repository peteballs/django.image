from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.upload_image, name = 'index' ),
    path('upload/', views.upload_image, name = 'image' ),
]
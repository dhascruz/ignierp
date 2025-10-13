from django.urls import path
from . import views

from django.urls import path
from . import  views_api

urlpatterns = [
    
    path('api/approved/', views_api.approved_blogs, name='approved_blogs_api'),
]
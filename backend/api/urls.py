from django.urls import path
from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import ProductListView, UserRegisterView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', UserRegisterView.as_view, name="register"),
    path('login/', views.login, name='login'),
    #I created a temp function to make sure the email was sent
    path('temp/', views.temp_email ,name='temp_email'),
    path('newsletter/', views.newsletter, name="newsletter"),
    path('products/', ProductListView.as_view(), name="products")
    
]

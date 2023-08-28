
from django.urls import path
from app_portifolio import views

urlpatterns = [
  path('',views.home, name= 'home')
]

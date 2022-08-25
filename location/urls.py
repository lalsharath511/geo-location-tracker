from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userdetails/', views.userdetails, name='userdetails')
]

from django.urls import path
from . import views

urlpatterns = [

    path('', views.Ragisterpage, name='ragisterpage'),
    path('ragister/', views.Ragister, name='ragister'),
    path('loginpage/', views.Loginpage, name='loginpage'),
    path('login/', views.Login, name='login'),
]

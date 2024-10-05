from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login-register/<str:action>/', views.login_register, name='login-register'),
]

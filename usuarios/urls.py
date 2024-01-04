from django.urls import path
from django.contrib.auth.views import PasswordResetView
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('user_login/', views.logar, name='user_login'),
    path('logout/', views.deslogar, name='deslogar'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
      
]

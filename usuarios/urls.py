from django.contrib import admin 
from django.urls import path
from .views import novo_usuario, loginPage, logoutUsuario

urlpatterns = [
    path('cadastrar/', novo_usuario, name='novo_usuario'),
    path('logar/', loginPage, name='login'),
    path('logout/', logoutUsuario, name='logout'),

]
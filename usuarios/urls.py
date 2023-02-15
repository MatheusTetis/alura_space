from django.urls import path
from usuarios.views import cadastro, favorito, login, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('favorito', favorito, name='favorito'),
]
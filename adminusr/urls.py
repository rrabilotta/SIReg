from django.urls import path
from .views import register_usuarioInterno, LogIn, logOut


urlpatterns = [
    path('register/',register_usuarioInterno , name='register'),
    path('logout/',logOut, name='logout'),
    path('login/', LogIn, name='login')
]

from django.urls import path, include, re_path
from .views import about


urlpatterns = [

    path('/about/',about,name='about' )
]

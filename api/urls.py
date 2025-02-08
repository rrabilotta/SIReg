from django.urls import path, include, re_path
from ninja import NinjaAPI
from api.api import router

api = NinjaAPI(version="1.0")
api.add_router("/api/v1/", router)

urlpatterns = [
    path("", api.urls),
]

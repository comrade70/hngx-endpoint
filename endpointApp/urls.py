from django.urls import path
from endpointApp.views import api

urlpatterns = [
    path("api", api, name = "api")
]

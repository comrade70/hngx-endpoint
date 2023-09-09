from django.urls import path
from endpointApp.views import user_details

urlpatterns = [
    path("user_details/", user_details, name = "user_details")
]

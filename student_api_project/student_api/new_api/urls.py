from django.conf.urls import url
from rest_framework import routers
from new_api.views import StudentApiView
from django.urls import path, include


urlpatterns = [
    path('students/', StudentApiView.as_view())
]

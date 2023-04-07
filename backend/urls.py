from django.contrib import admin
from django.urls import path, re_path, include
from participants import views

from django.urls import include, path

from rest_framework import routers
from participants.views import ParticipantViewSet

api_router = routers.DefaultRouter()
api_router.register(r"participants", ParticipantViewSet)

urlpatterns = [
    path("", include(api_router.urls)),
]
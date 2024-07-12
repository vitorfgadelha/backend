from django.urls import path, include
from rest_framework.routers import DefaultRouter
from participants.views import ParticipantViewSet, EventViewSet

# Cria um router para API
router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'participants', ParticipantViewSet)

# URLs da aplicação
urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoodleUserViewSet

router = DefaultRouter()
router.register(r"moodle-users", MoodleUserViewSet, basename="moodle-user")

urlpatterns = [
    # API endpoints
    path("", include(router.urls)),

    # HTML page
    
]
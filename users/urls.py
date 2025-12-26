from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoodleUserViewSet, api_teacher_login,api_admin_login

router = DefaultRouter()
router.register(r"moodle-users", MoodleUserViewSet, basename="moodle-user")

urlpatterns = [
    # API endpoints
    path("", include(router.urls)),
    path("teachers/login/", api_teacher_login, name="api_teacher_login"),
    path("admin/login/", api_admin_login, name="api_admin_login"),
    # HTML page
    
]
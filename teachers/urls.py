from django.urls import path
from .views import *


urlpatterns = [
    
    path("login/", login_view, name="teacher_login"),
    path("logout/", teacher_logout, name="teacher_logout"),
    path("dashboard/", dashboard_view, name="teacher_dashboard"),
    path("courses/", courses_view, name="teacher_courses"),
    path("courses/<int:course_id>/students/", course_students_view, name="course_students"),
]

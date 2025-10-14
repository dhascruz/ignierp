from django.urls import path, include
from .views import *


urlpatterns = [
    
    path("login/", login_view, name="teacher_login"),
    path("logout/", teacher_logout, name="teacher_logout"),
    path("dashboard/", dashboard_view, name="teacher_dashboard"),
    path("mycourses/", mycourses_view, name="teacher_mycourses"),

    path("courses/", courses_view, name="teacher_courses"),
    path("courses/<int:course_id>/students/", course_students_view, name="course_students"),
    path('create_blog/', create_post, name='create_post'),
     path('blogs/edit/<int:post_id>/', edit_post, name='edit_post'),
    
    path('blogs/', blog_list, name='blog_list'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

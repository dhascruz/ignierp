from django.urls import path

from users.views import category_list, cohort_list, course_list_byid
from .views import user_list

urlpatterns = [
    path("user_list/", user_list, name="user_list"),
    path("cohorts_list/", cohort_list, name="cohorts_list"),
    
]

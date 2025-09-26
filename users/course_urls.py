from django.urls import path

from users.views import category_list, cohort_list, course_list_byid
from .views import enrolled_users, user_list

urlpatterns = [
    path("categories_list/", category_list, name="categories_list"),
    path("courses_list/<int:category_id>/", course_list_byid, name="courses_list"),
    path("enrolled_users/<int:course_id>/", enrolled_users, name="enrolled_users"),
]

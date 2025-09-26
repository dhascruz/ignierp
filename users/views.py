from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import render

from users.services import get_cohort_counts, get_course_categories, get_course_teachers_students, get_courses_by_category, get_enrolled_users
from .serializers import MoodleUserSerializer
#from .services import moodle_user 
from django.db.models import F
from django.db.models import Q
from .models import  *
from .services import get_users_with_roles


class MoodleUserViewSet(viewsets.ViewSet):

    def list(self, request):
        """Return all Moodle users"""
        result = moodle_user.get_all_users()

        users = result.get("users", []) if isinstance(result, dict) else []
        
        return Response(users)


    def create(self, request):
        serializer = MoodleUserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            result = moodle_user.create_user(
                data["username"], data["password"],
                data["firstname"], data["lastname"], data["email"]
            )
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        result = moodle_user.get_user_by_id(pk)
        return Response(result)

    def update(self, request, pk=None):
        result = moodle_user.update_user(pk, **request.data)
        return Response(result)

    def destroy(self, request, pk=None):
        result = moodle_user.delete_user(pk)
        return Response(result, status=status.HTTP_204_NO_CONTENT)




#@login_required
def user_list(request):
    users = get_users_with_roles()  # Returns a list or queryset
    print(users)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(users, 10)  # 10 users per page

    try:
        users_page = paginator.page(page)
    except PageNotAnInteger:
        users_page = paginator.page(1)
    except EmptyPage:
        users_page = paginator.page(paginator.num_pages)

    return render(request, "users_list.html", {"users": users_page})


@login_required
def cohort_list(request):
    cohort_list = get_cohort_counts()  # Returns a list or queryset
    print(cohort_list)

    # Pagination
    page = request.GET.get('page', 1)  # Current page number from query parameter
    paginator = Paginator(cohort_list, 10)  # Show 10 cohorts per page

    try:
        cohorts = paginator.page(page)
    except PageNotAnInteger:
        cohorts = paginator.page(1)
    except EmptyPage:
        cohorts = paginator.page(paginator.num_pages)

    return render(request, "cohorts_list.html", {"cohorts": cohorts})

  
@login_required
def category_list(request):
    category_list = get_course_categories()  # Returns a list or queryset
    print(category_list)

    # Pagination
    page = request.GET.get('page', 1)  # Current page number
    paginator = Paginator(category_list, 10)  # Show 10 categories per page

    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)

    return render(request, "categories_list.html", {"categories": categories})




# def home(request):
#     category_list = get_course_categories()
#     print(category_list)
#     return render(request, "home.html", {"categories": category_list})    





from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def course_list_byid(request, category_id):
    courses = get_course_teachers_students(category_id)  # Returns a list or queryset
    print(courses)

    # Pagination
    page = request.GET.get('page', 1)  # Get current page number from query parameter
    paginator = Paginator(courses, 10)  # Show 10 courses per page

    try:
        courses_page = paginator.page(page)
    except PageNotAnInteger:
        courses_page = paginator.page(1)
    except EmptyPage:
        courses_page = paginator.page(paginator.num_pages)

    return render(request, "courses_list.html", {"courses": courses_page})


def enrolled_users(request, course_id):
    enrolled_users_list = get_enrolled_users(course_id)  # Returns a list or queryset
    print(enrolled_users_list)

    # Pagination
    page = request.GET.get('page', 1)  # Get current page number from query parameter
    paginator = Paginator(enrolled_users_list, 10)  # Show 10 users per page

    try:
        users_page = paginator.page(page)
    except PageNotAnInteger:
        users_page = paginator.page(1)
    except EmptyPage:
        users_page = paginator.page(paginator.num_pages)

    return render(request, "enrolled_users.html", {"enrolled_users": users_page})
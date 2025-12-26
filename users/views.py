from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import User

from teachers.utils import check_moodle_password
from users.services import get_cohort_counts, get_course_categories, get_course_teachers_students, get_courses_by_category, get_enrolled_users
from .serializers import MoodleUserSerializer
#from .services import moodle_user 
from django.db.models import F
from django.db.models import Q
from .models import  *
from teachers.models import TeacherMoodleUser   
#from .utils import moodle_user
from users.utils import run_course_backup
from .services import get_users_with_roles

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


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


def trigger_backup(request, course_id):
    #destination = "/home/u875591253/backup/"
    destination = "/home/dhas/backup/"

    output = run_course_backup(course_id, destination)

    print(output)
    # Show latest backups
    backups = CourseBackup.objects.filter(course_id=course_id).order_by("-created_at")

    return render(request, "backup_result.html", {
        "course_id": course_id,
        "output": output,
        "backups": backups
    })    



@csrf_exempt
@require_POST
def api_teacher_login(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        print("Attempting login for user:", username)
        print("Attempting login for user:", password)
    

        # user = authenticate(request, username=username, password=password)

        user = TeacherMoodleUser.objects.using("moodle").get(username=username)

        # return JsonResponse({
        #     "success": True, 
        #     "username": user,
        #     "message": "Login successful"        })
        #     # ✅ Verify password using your he  lper
            

        if check_moodle_password(password, user.password):
            # ✅ Sync or create a Django User
                django_user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        "first_name": user.firstname,
                        "last_name": user.lastname,
                        "email": getattr(user, "email", ""),
                    }
                )

                # Optionally update name/email if Moodle data changed
                if not created:
                    django_user.first_name = user.firstname
                    django_user.last_name = user.lastname
                    django_user.email = getattr(user, "email", "")
                    django_user.save()

                # ✅ Log the Django user in
                login(request, django_user)

                # ✅ (Optional) Store Moodle info in session
                request.session["userid"] = user.id
                request.session["fullname"] = f"{user.firstname} {user.lastname}"

                return JsonResponse({
                "success": True,
                "username": username,
                "password": password,
                "message": "valid credentials"
             }, status=200)

        else:
            return JsonResponse({
                "success": False,
                "username": username,
                "password": password,
                "message": "Invalid credentials"
             }, status=401)

    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": str(e)
        }, status=400)




@csrf_exempt
@require_POST
def api_teacher_login(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        print("Attempting login for user:", username)
        print("Attempting login for user:", password)
    

        # user = authenticate(request, username=username, password=password)

        user = TeacherMoodleUser.objects.using("moodle").get(username=username)

        # return JsonResponse({
        #     "success": True, 
        #     "username": user,
        #     "message": "Login successful"        })
        #     # ✅ Verify password using your he  lper
            

        if check_moodle_password(password, user.password):
            # ✅ Sync or create a Django User
                django_user, created = User.objects.get_or_create(
                    username=username,
                    defaults={
                        "first_name": user.firstname,
                        "last_name": user.lastname,
                        "email": getattr(user, "email", ""),
                    }
                )

                # Optionally update name/email if Moodle data changed
                if not created:
                    django_user.first_name = user.firstname
                    django_user.last_name = user.lastname
                    django_user.email = getattr(user, "email", "")
                    django_user.save()

                # ✅ Log the Django user in
                login(request, django_user)

                # ✅ (Optional) Store Moodle info in session
                request.session["userid"] = user.id
                request.session["fullname"] = f"{user.firstname} {user.lastname}"

                return JsonResponse({
                "success": True,
                "username": username,
                "password": password,
                "message": "valid credentials"
             }, status=200)

        else:
            return JsonResponse({
                "success": False,
                "username": username,
                "password": password,
                "message": "Invalid credentials"
             }, status=401)

    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": str(e)
        }, status=400)



@csrf_exempt
@require_POST
def api_admin_login(request):
    try:
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return JsonResponse({
                "success": False,
                "message": "Username and password required"
            }, status=400)

        print("Admin login attempt:", username)

        user = authenticate(request, username=username, password=password)

        
        # ❌ Invalid credentials
        if user is None:
            return JsonResponse({
                "success": False,
                "message": "Invalid username or password"
            }, status=401)

        # ❌ Not an admin
        if not (user.is_staff or user.is_superuser):
            return JsonResponse({
                "success": False,
                "message": "Not authorized as admin"
            }, status=403)

        # ✅ Login success
        login(request, user)

        return JsonResponse({
            "success": True,
            "username": user.username,
            "message": "Admin login successful",
            "redirect_url": "/erp/admin/dashboard/"
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": str(e)
        }, status=400)
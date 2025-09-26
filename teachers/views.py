from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import TeacherProfile
from .serializers import TeacherLoginSerializer
from .moodle_client import get_moodle_token, get_moodle_user_info
from django.shortcuts import render, redirect
from django.contrib import messages
from .moodle_client import get_moodle_token, get_moodle_user_info, get_moodle_courses

from teachers.services import get_teacher_courses, get_teacher_courses_with_student_count, get_students_for_course
from .models import TeacherMoodleUser




from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connections
from .models import *
from .utils import check_moodle_password

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(username, password)

        try:
            user = TeacherMoodleUser.objects.using("moodle").get(username=username)

            if check_moodle_password(password, user.password):
                # Save Moodle user info in session
                request.session["userid"] = user.id
                request.session["fullname"] = f"{user.firstname} {user.lastname}"
                print("session", request.session["userid"])
                print("session", request.session["fullname"])
                print("Login successful")
                return redirect("teacher_dashboard")  # ✅ redirect to dashboard
            else:
                messages.error(request, "Invalid username or password")

        except TeacherMoodleUser.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, "teachers/login.html")  # your Metronic login template


#@login_required
def teacher_logout(request):
    """
    Logs out the currently logged-in teacher and redirects to the login page.
    """
    logout(request)
    return redirect('teacher_login')  # Replace with your login URL name


def dashboard_view(request):
    userid = request.session.get("userid")
    fullname = request.session.get("fullname")
    print("UserID:", userid, "Fullname:", fullname)

    if not fullname:
        return redirect("teacher_login")  # if not logged in, send back to login
    
    courses = get_teacher_courses_with_student_count(userid)

    return render(request, "teachers/dashboard.html", {
        "fullname": fullname,
        "courses": courses
    })


def courses_view(request):
    userid = request.session.get("userid")
    fullname = request.session.get("fullname")

    if not userid:
        return redirect("teacher_login")

    courses = get_teacher_courses_with_student_count(userid)
    

    return render(request, "teachers/courses.html", {
        "fullname": fullname,
        "courses": courses
    })




def course_students_view(request, course_id):
    teacher_id = request.session.get("userid")
    fullname = request.session.get("fullname")

    if not teacher_id:
        return redirect("teacher_login")

    students = get_students_for_course(course_id, teacher_id)

    # Pagination
    page = request.GET.get('page', 1)  # Get current page number from query parameter
    paginator = Paginator(students, 10)  # Show 10 students per page

    try:
        students_page = paginator.page(page)
    except PageNotAnInteger:
        students_page = paginator.page(1)
    except EmptyPage:
        students_page = paginator.page(paginator.num_pages)

    return render(request, "teachers/mystudents.html", {
        "fullname": fullname,
        "students": students_page,
        "course_id": course_id
    })
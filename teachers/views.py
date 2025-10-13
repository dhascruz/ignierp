from urllib import request
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


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
from users.models import CourseBackup



from django.conf import settings



from django.shortcuts import render, redirect,get_object_or_404 

from django.db import connections
from .models import *
from blog.models import BlogPost    
from blog.forms  import BlogPostForm
from .utils import check_moodle_password



from django.contrib.auth import login


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # ✅ Lookup Moodle user in external DB
            user = TeacherMoodleUser.objects.using("moodle").get(username=username)

            # ✅ Verify password using your helper
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

                return redirect("teacher_dashboard")

            else:
                messages.error(request, "Invalid username or password")

        except TeacherMoodleUser.DoesNotExist:
            messages.error(request, "User not found")

    return render(request, "teachers/login.html")# your Metronic login template


@login_required
def teacher_logout(request):
    """
    Logs out the currently logged-in teacher and redirects to the login page.
    """
    logout(request)
    return redirect('teacher_login')  # Replace with your login URL name


@login_required(login_url='/erp/teachers/login/')
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


@login_required(login_url='/erp/teachers/login/')
def courses_view(request):
    # Get Moodle session info (set at login)
    userid = request.session.get("userid")
    fullname = request.session.get("fullname")

    # Extra safety: redirect if Moodle session info missing
    if not userid:
        return redirect("teacher_login")  # Django URL name for login page

    # Fetch courses for this teacher
    courses = get_teacher_courses_with_student_count(userid)

    return render(request, "teachers/courses.html", {
        "fullname": fullname,
        "courses": courses
    })

@login_required
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






@login_required
def create_post(request):
    # Check if logged-in user is a teacher
    # if not hasattr(request.user, 'teacher'):
    #     return HttpResponseForbidden("Only teachers can create posts.")

    print("Request User:", request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('/erp/teachers/blogs')
    else:
        form = BlogPostForm()
    return render(request, 'teachers/blog_create.html', {'form': form})


@login_required(login_url='/erp/teachers/login/')
def edit_post(request, post_id):
    """
    Edit a blog post by ID — only the author (teacher) can edit their own post.
    """
    # Get the post; ensure the current user is the author
    blog_post = get_object_or_404(BlogPost, id=post_id, author=request.user)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.status = 'pending'  # reset status so admin must re-approve
            post.save()
            form.save_m2m()
            return redirect('/erp/teachers/blogs')
    else:
        form = BlogPostForm(instance=blog_post)

    return render(request, 'teachers/blog_create.html', {
        'form': form,
        'blog_post': blog_post,
        'action': 'Edit',
    })

@login_required
def blog_list(request):
    posts = BlogPost.objects.filter(status='approved').order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

@login_required(login_url='/erp/teachers/login/')
def blog_list(request):
    # Filter only approved posts by the logged-in teacher
    print("Request User:", request.user)
    posts = BlogPost.objects.filter(
        
        author=request.user
    ).order_by('-created_at')

    print("Posts:", posts)
    return render(request, 'teachers/blogs.html', {'posts': posts})  
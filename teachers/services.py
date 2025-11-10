from django.db import connections

def get_teacher_courses(userid):
    query = """
        SELECT c.id AS course_id,
               c.fullname AS course_name,
               c.shortname AS course_shortname
        FROM mdl_course c
        JOIN mdl_context ctx ON ctx.instanceid = c.id
        JOIN mdl_role_assignments ra ON ra.contextid = ctx.id
        JOIN mdl_role r ON r.id = ra.roleid
        JOIN mdl_user u ON u.id = ra.userid
        WHERE ctx.contextlevel = 50
          AND u.id = %s
          AND r.shortname IN ('editingteacher', 'teacher')
    """
    with connections['moodle'].cursor() as cursor:
        cursor.execute(query, [userid])
        rows = cursor.fetchall()
        return [{"id": row[0], "fullname": row[1], "shortname": row[2]} for row in rows]

import os
import requests
from django.conf import settings
from django.core.files.base import ContentFile

def get_teacher_courses_with_student_count(userid):
    query = """
        SELECT 
            c.id AS course_id,
            c.fullname AS course_name,
            c.shortname AS course_shortname,
            COUNT(DISTINCT u2.id) AS student_count,
            ctx.id AS context_id,
            f.filename AS course_image
        FROM mdl_course c
        JOIN mdl_context ctx ON ctx.instanceid = c.id AND ctx.contextlevel = 50
        JOIN mdl_role_assignments ra ON ra.contextid = ctx.id
        JOIN mdl_role r ON r.id = ra.roleid
        JOIN mdl_user u ON u.id = ra.userid
        LEFT JOIN mdl_enrol e ON e.courseid = c.id
        LEFT JOIN mdl_user_enrolments ue ON ue.enrolid = e.id
        LEFT JOIN mdl_user u2 ON u2.id = ue.userid AND u2.deleted = 0 AND u2.suspended = 0
        LEFT JOIN mdl_files f 
            ON f.contextid = ctx.id 
            AND f.component = 'course'
            AND f.filearea = 'overviewfiles'
            AND f.filename <> '.'
        WHERE u.id = %s
          AND r.shortname IN ('editingteacher', 'teacher')
        GROUP BY c.id, c.fullname, c.shortname, ctx.id, f.filename
        ORDER BY c.fullname
    """

    with connections['moodle'].cursor() as cursor:
        cursor.execute(query, [userid])
        rows = cursor.fetchall()

    #moodle_base_url = "http://210.18.177.188/igni/pluginfile.php"
    moodle_base_url=   settings.MOODLE_BASE_URL.rstrip('/')+"/pluginfile.php"
    moodle_base_url2 = settings.MOODLE_BASE_URL.rstrip('/')

    local_folder = os.path.join(settings.MEDIA_ROOT, "course_images")
    os.makedirs(local_folder, exist_ok=True)

    courses = []

    for row in rows:
        course_id, course_name, course_shortname, student_count, context_id, course_image = row

        local_image_url = None
        moodle_course_url = None
        if course_image:
            # Build the full Moodle image URL
            moodle_image_url = f"{moodle_base_url}/{context_id}/course/overviewfiles/{course_image}"
            moodle_course_url = f"{moodle_base_url2}/course/view.php?id={course_id}"
	        

            try:
                print(moodle_course_url)
                response = requests.get(moodle_image_url, timeout=10)
                if response.status_code == 200:
                    # Save locally in MEDIA_ROOT/course_images/
                    local_filename = f"{course_id}_{course_image}"
                    local_path = os.path.join(local_folder, local_filename)

                    with open(local_path, "wb") as f:
                        f.write(response.content)

                    # Publicly accessible URL
                    local_image_url = f"{settings.MEDIA_URL}course_images/{local_filename}"

            except Exception as e:
                print(f"⚠️ Could not download {moodle_image_url}: {e}")

        courses.append({
            "id": course_id,
            "fullname": course_name,
            "shortname": course_shortname,
            "student_count": student_count,
            "image_url": local_image_url,
            "course_url": moodle_course_url,

        })

    return courses



from django.db import connections

def get_students_for_course(course_id, teacher_id):
    query = """
        SELECT u.id AS student_id,
               u.username,
               u.firstname,
               u.lastname,
               u.email
        FROM mdl_user u
        JOIN mdl_user_enrolments ue ON ue.userid = u.id
        JOIN mdl_enrol e ON e.id = ue.enrolid
        JOIN mdl_course c ON c.id = e.courseid
        JOIN mdl_context ctx ON ctx.instanceid = c.id
        JOIN mdl_role_assignments ra ON ra.contextid = ctx.id
        JOIN mdl_role r ON r.id = ra.roleid
        WHERE ctx.contextlevel = 50
          AND c.id = %s
          AND r.shortname IN ('editingteacher','teacher')
          AND ra.userid = %s
          AND u.deleted = 0
          AND u.suspended = 0
        ORDER BY u.lastname, u.firstname
    """

    with connections['moodle'].cursor() as cursor:
        cursor.execute(query, [course_id, teacher_id])
        rows = cursor.fetchall()

    students = []
    for row in rows:
        student_id, username, firstname, lastname, email = row
        students.append({
            "id": student_id,
            "username": username,
            "firstname": firstname,
            "lastname": lastname,
            "email": email
        })

    return students

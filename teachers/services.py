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



def get_teacher_courses_with_student_count(userid):
    query = """
        SELECT c.id AS course_id,
               c.fullname AS course_name,
               c.shortname AS course_shortname,
               COUNT(DISTINCT u2.id) AS student_count
        FROM mdl_course c
        JOIN mdl_context ctx ON ctx.instanceid = c.id
        JOIN mdl_role_assignments ra ON ra.contextid = ctx.id
        JOIN mdl_role r ON r.id = ra.roleid
        JOIN mdl_user u ON u.id = ra.userid
        -- Join to count students
        LEFT JOIN mdl_enrol e ON e.courseid = c.id
        LEFT JOIN mdl_user_enrolments ue ON ue.enrolid = e.id
        LEFT JOIN mdl_user u2 ON u2.id = ue.userid AND u2.deleted = 0 AND u2.suspended = 0
        WHERE ctx.contextlevel = 50
          AND u.id = %s
          AND r.shortname IN ('editingteacher', 'teacher')
        GROUP BY c.id, c.fullname, c.shortname
        ORDER BY c.fullname
    """

    with connections['moodle'].cursor() as cursor:
        cursor.execute(query, [userid])
        rows = cursor.fetchall()

    # Format results
    courses = []
    for row in rows:
        course_id, course_name, course_shortname, student_count = row
        courses.append({
            "id": course_id,
            "fullname": course_name,
            "shortname": course_shortname,
            "student_count": student_count
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

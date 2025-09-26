

from django.db import connections

def get_users_with_roles():
    query = """
        SELECT 
            u.id AS user_id,
            u.username,
            u.firstname,
            u.lastname,
            u.email,
            GROUP_CONCAT(DISTINCT r.shortname ORDER BY r.id SEPARATOR ', ') AS roles
        FROM mdl_user u
        LEFT JOIN mdl_role_assignments ra ON ra.userid = u.id
        LEFT JOIN mdl_role r ON r.id = ra.roleid
        LEFT JOIN mdl_context ctx ON ctx.id = ra.contextid
        WHERE u.deleted = 0
        GROUP BY u.id, u.username, u.firstname, u.lastname, u.email
        ORDER BY u.id
    """
    with connections['moodle'].cursor() as cursor:  # ✅ use 'moodle' connection
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


def get_cohort_counts():
    query = """
       SELECT 
    c.id AS cohort_id,
    c.name AS cohort_name,
    c.idnumber AS cohort_code,
    COUNT(cm.userid) AS user_count
FROM mdl_cohort c
LEFT JOIN mdl_cohort_members cm ON cm.cohortid = c.id
LEFT JOIN mdl_user u ON u.id = cm.userid AND u.deleted = 0
GROUP BY c.id, c.name, c.idnumber
ORDER BY c.id;

    """
    with connections['moodle'].cursor() as cursor:  # ✅ use 'moodle' connection
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()] 



def get_course_categories():
    query = """
        SELECT 
            c.id AS category_id,
            c.name AS category_name,
            c.parent AS parent_id,
            COUNT(co.id) AS course_count
        FROM mdl_course_categories c
        LEFT JOIN mdl_course co ON co.category = c.id
        GROUP BY c.id, c.name, c.parent
        ORDER BY c.id;
    """
    with connections['moodle'].cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


def get_courses_by_category(category_id):
    query = """
        SELECT 
            co.id AS course_id,
            co.fullname AS course_name,
            co.shortname AS course_code,
            co.summary,
            co.visible,
            c.id AS category_id,
            c.name AS category_name
        FROM mdl_course co
        JOIN mdl_course_categories c ON c.id = co.category
        WHERE co.category = %s
        ORDER BY co.id;
    """
    with connections['moodle'].cursor() as cursor:
        cursor.execute(query, [category_id])
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


def get_course_teachers_students(category_id):
    query = """
        SELECT
            co.id AS course_id,
            co.fullname AS course_name,
            co.shortname AS course_code,
            SUM(CASE WHEN r.shortname IN ('editingteacher','teacher') THEN 1 ELSE 0 END) AS teacher_count,
            SUM(CASE WHEN r.shortname = 'student' THEN 1 ELSE 0 END) AS student_count,
            GROUP_CONCAT(DISTINCT 
                CASE WHEN r.shortname IN ('editingteacher','teacher') 
                     THEN CONCAT(u.firstname, ' ', u.lastname)
                END
                ORDER BY u.lastname, u.firstname
                SEPARATOR ', '
            ) AS teacher_names,
            GROUP_CONCAT(DISTINCT ch.name ORDER BY ch.name SEPARATOR ', ') AS cohorts
        FROM mdl_course co
        JOIN mdl_context ctx ON ctx.instanceid = co.id AND ctx.contextlevel = 50
        LEFT JOIN mdl_role_assignments ra ON ra.contextid = ctx.id
        LEFT JOIN mdl_role r ON r.id = ra.roleid
        LEFT JOIN mdl_user u ON u.id = ra.userid
        LEFT JOIN mdl_cohort_members cm ON cm.userid = u.id
        LEFT JOIN mdl_cohort ch ON ch.id = cm.cohortid
        WHERE co.category = %s
        GROUP BY co.id, co.fullname, co.shortname
        ORDER BY co.id;
    """
    with connections['moodle'].cursor() as cursor:
        cursor.execute(query, [category_id])
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    
def get_enrolled_users(course_id):
    query = """
        SELECT
            u.id AS user_id,
            u.username,
            CONCAT(u.firstname, ' ', u.lastname) AS full_name,
            u.email,
            r.shortname AS role_name,
            GROUP_CONCAT(DISTINCT ch.name ORDER BY ch.name SEPARATOR ', ') AS cohorts,
            GROUP_CONCAT(DISTINCT g.name ORDER BY g.name SEPARATOR ', ') AS groups
        FROM mdl_user u
        JOIN mdl_role_assignments ra ON ra.userid = u.id
        JOIN mdl_role r ON r.id = ra.roleid
        JOIN mdl_context ctx ON ctx.id = ra.contextid AND ctx.contextlevel = 50
        JOIN mdl_course co ON co.id = ctx.instanceid
        LEFT JOIN mdl_cohort_members cm ON cm.userid = u.id
        LEFT JOIN mdl_cohort ch ON ch.id = cm.cohortid
        LEFT JOIN mdl_groups_members gm ON gm.userid = u.id
        LEFT JOIN mdl_groups g ON g.id = gm.groupid AND g.courseid = co.id
        WHERE co.id = %s
        GROUP BY u.id, u.username, full_name, u.email, r.shortname
        ORDER BY role_name DESC, full_name;
    """
    with connections['moodle'].cursor() as cursor:
        cursor.execute(query, [course_id])
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]    
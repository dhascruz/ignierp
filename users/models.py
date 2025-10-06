from django.db import models
from django.utils import timezone

class MoodleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    deleted = models.BooleanField(default=False)

    class Meta:
        managed = False  # prevent Django migrations
        db_table = "mdl_user"


class MoodleRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "mdl_role"


class MoodleContext(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextlevel = models.IntegerField()

    class Meta:
        managed = False
        db_table = "mdl_context"


class MoodleRoleAssignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.ForeignKey(MoodleUser, on_delete=models.CASCADE, db_column="userid")
    roleid = models.ForeignKey(MoodleRole, on_delete=models.CASCADE, db_column="roleid")
    contextid = models.ForeignKey(MoodleContext, on_delete=models.CASCADE, db_column="contextid")

    class Meta:
        managed = False
        db_table = "mdl_role_assignments"



class CourseBackup(models.Model):
    course_id = models.IntegerField()
    file_path = models.CharField(max_length=500)
    status = models.CharField(max_length=50, default="pending")  # pending, success, failed
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Course {self.course_id} -> {self.file_path}"    
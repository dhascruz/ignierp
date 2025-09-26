from django.db import models
from django.contrib.auth.models import User

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    moodle_token = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username



class TeacherMoodleUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # hashed password
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        managed = False  # Django will not create/alter this table
        db_table = "mdl_user"
        app_label = "teachers"
from rest_framework import serializers
from django.contrib.auth.models import User

class TeacherLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

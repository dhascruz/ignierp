from rest_framework import serializers

class MoodleUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=False)

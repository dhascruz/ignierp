from rest_framework import serializers
from blog.models import BlogPost

class MoodleUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, required=False)



class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    tags = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name'
    )

    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'content',
            'author_name',
            'image',
            'tags',
            'published_date',
        ]
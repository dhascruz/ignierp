# blog/serializers.py
from rest_framework import serializers
from .models import BlogPost

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

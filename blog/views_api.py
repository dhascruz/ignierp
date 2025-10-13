# blog/views_api.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

@api_view(['GET'])
def approved_blogs(request):
    posts = BlogPost.objects.filter(status='approved').order_by('-published_date')
    
    serializer = BlogPostSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data)

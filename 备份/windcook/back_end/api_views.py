from .blog import models as BlogModel



from .serializers import BlogListSerializer,BlogTagSerializer
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

class BlogList(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = BlogModel.Blog.objects.all()
    serializer_class = BlogListSerializer
    '''
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


    def get(self, request, format=None):
        blog = Blog.objects.all()
        serializer = BlogListSerializer(blog, many=True)
        return Response(serializer.data)
        '''
class BlogTagList(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    List all snippets, or create a new snippet.
    """
    queryset = BlogModel.BlogTag.objects.all()
    serializer_class = BlogTagSerializer
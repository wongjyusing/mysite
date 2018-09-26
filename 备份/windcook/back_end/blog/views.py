from django.shortcuts import render

# Create your views here.
from .models import Blog,BlogTag
from .serializers import BlogListSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class SnippetList(generics.ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer
    '''
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    
    def get(self, request, format=None):
        blog = Blog.objects.all()
        serializer = BlogListSerializer(blog, many=True)
        return Response(serializer.data)
        '''

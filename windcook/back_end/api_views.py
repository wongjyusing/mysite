from django.http import Http404,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .blog import models as BlogModels

import markdown


class BlogList(APIView):
    """
    List all blog
    """
    def get(self, request, format=None):
        context = {}

        blog = BlogModels.Blog.objects.all()
        blogSerializer = serializers.BlogListSerializer(blog, many=True)
        blog_tag = BlogModels.BlogTag.objects.all()
        context['blogs'] = blogSerializer.data
        return Response(context)


class BlogDetail(APIView):
    """
    Detail Blog Data
    """
    def get_object(self, slug):
        try:
            return BlogModels.Blog.objects.get(slug=slug)
        except BlogModels.Blog.DoesNotExist:

            raise Http404

    def get(self, request, slug, format=None):
        context = {}
        blog = self.get_object(slug)

        serializer = serializers.BlogDeatilSerializer(blog)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            ])

        context['blog'] = serializer.data
        context['blog']['body'] = md.convert(context['blog']['body'])
        context['blog']['toc'] = md.toc
        context['blog']['created_time'] = context['blog']['created_time'][0:10]
        return Response(context)


class BlogTagList(APIView):
    """
    Detail Blog Data
    """
    def get_object(self, slug):
        try:
            tags = BlogModels.BlogTag.objects.get(slug=slug)
            blogs = BlogModels.Blog.objects.filter(blog_tag=tags)
            return tags,blogs
        except BlogModels.BlogTag.DoesNotExist:

            raise Http404

    def get(self, request, slug, format=None):
        context = {}
        tags,blogs = self.get_object(slug)
        serializer = serializers.TagListSerializer(tags)
        context['blog_tag'] = serializer.data
        context['blogs'] = serializers.BlogListSerializer(blogs, many=True).data
        return Response(context)

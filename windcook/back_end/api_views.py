from django.http import Http404,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .blog import models as BlogModels
from .toolbox import models as ToolBoxModels
import markdown
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class BlogBase(APIView):
    def page_gen(self,contact_list,page):

        paginator = Paginator(contact_list, 10,2)  # Show 10 contacts per page

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)

        return contacts

class BlogList(BlogBase):
    """
    List all blog
    """


    def get(self, request, format=None):
        context = {}
        page = request.GET.get('page',1)

        context['friend_link'] = serializers.FriendLinkSerializer(ToolBoxModels.FriendLink.objects.all(),many=True).data
        context['space_link'] = serializers.BookLinkSerializer(ToolBoxModels.SpaceLink.objects.all(),many=True).data
        context['book_link'] = serializers.SpaceLinkSerializer(ToolBoxModels.BookLink.objects.all(),many=True).data
        context['toolbox_tags'] = serializers.BlogListTagSerializer(BlogModels.BlogTag.objects.all(),many=True).data

        blogs = self.page_gen(BlogModels.Blog.objects.all(),page)
        page_list = re.findall('<bound method Page.has_other_pages of <Page (.*?) of (.*?)>>',string=str(blogs.has_other_pages))

        context['page'] = {'now_page':page_list[0][0],'page_count':page_list[0][1]}
        context['blogs'] = serializers.BlogListSerializer(blogs, many=True).data
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
        # 上一篇和下一篇
        try:
            context['next'] = {'slug':blog.get_next().slug,'title':blog.get_next().title}
        except Exception as e:
            context['next'] = {'slug':'#','title':'现在阁下浏览到最后一篇了'}
        try:
            context['previous'] = {'slug':blog.get_pre().slug,'title':blog.get_pre().title}
        except Exception as e:
            context['previous'] = {'slug':'#','title':'现在阁下浏览的是第一篇文章'}
        #context['previous'] = {'slug':blog.get_pre().slug,'title':blog.get_pre().title}
        #context['next'] = [blog.get_next().slug,blog.get_next().title]

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


class BlogTagList(BlogBase):
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
        page = request.GET.get('page',1)
        tags,blogs = self.get_object(slug)

        context['friend_link'] = serializers.FriendLinkSerializer(ToolBoxModels.FriendLink.objects.all(),many=True).data
        context['space_link'] = serializers.BookLinkSerializer(ToolBoxModels.SpaceLink.objects.all(),many=True).data
        context['book_link'] = serializers.SpaceLinkSerializer(ToolBoxModels.BookLink.objects.all(),many=True).data
        context['toolbox_tags'] = serializers.BlogListTagSerializer(BlogModels.BlogTag.objects.all(),many=True).data


        context['blog_tag'] = serializers.TagListSerializer(tags).data


        blogs = self.page_gen(blogs,page)
        page_list = re.findall('<bound method Page.has_other_pages of <Page (.*?) of (.*?)>>',string=str(blogs.has_other_pages))

        context['page'] = {'now_page':page_list[0][0],'page_count':page_list[0][1]}
        context['blogs'] = serializers.BlogListSerializer(blogs, many=True).data

        return Response(context)

class BookList(APIView):
    def get(self, request, format=None):
        context = {}
        page = request.GET.get('page',1)
        context['gitbook'] = serializers.GitBookLinkSerializer(ToolBoxModels.GitBookLink.objects.all(),many=True).data
        context['friend_link'] = serializers.FriendLinkSerializer(ToolBoxModels.FriendLink.objects.all(),many=True).data
        context['space_link'] = serializers.BookLinkSerializer(ToolBoxModels.SpaceLink.objects.all(),many=True).data
        context['book_link'] = serializers.SpaceLinkSerializer(ToolBoxModels.BookLink.objects.all(),many=True).data
        context['toolbox_tags'] = serializers.BlogListTagSerializer(BlogModels.BlogTag.objects.all(),many=True).data


        return Response(context)


# 通用工具视图配置



class MySiteDatas(APIView):
    """
    List all blog
    """
    def get(self, request, format=None):
        context = {}

        toolbox = ToolBoxModels.MySiteData.objects.all()
        toolboxSerializer = serializers.SiteDataSerializer(toolbox, many=True)
        context['mysite'] = toolboxSerializer.data
        return Response(context)


class HomeViews(APIView):
    def get(self, request, format=None):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            ])
        context = {}
        context['friend_link'] = serializers.FriendLinkSerializer(ToolBoxModels.FriendLink.objects.all(),many=True).data
        context['space_link'] = serializers.BookLinkSerializer(ToolBoxModels.SpaceLink.objects.all(),many=True).data
        context['book_link'] = serializers.SpaceLinkSerializer(ToolBoxModels.BookLink.objects.all(),many=True).data
        context['toolbox_tags'] = serializers.BlogListTagSerializer(BlogModels.BlogTag.objects.all(),many=True).data
        context['home'] = serializers.HomeSerializer(ToolBoxModels.Home.objects.all(), many=True).data
        context['home'][0]['body'] = md.convert(context['home'][0]['body'])
        context['home'][0]['created_time'] = context['home'][0]['created_time'][0:10]
        return Response(context)


class AboutViews(APIView):
    def get(self, request, format=None):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            ])
        context = {}
        context['friend_link'] = serializers.FriendLinkSerializer(ToolBoxModels.FriendLink.objects.all(),many=True).data
        context['space_link'] = serializers.BookLinkSerializer(ToolBoxModels.SpaceLink.objects.all(),many=True).data
        context['book_link'] = serializers.SpaceLinkSerializer(ToolBoxModels.BookLink.objects.all(),many=True).data
        context['toolbox_tags'] = serializers.BlogListTagSerializer(BlogModels.BlogTag.objects.all(),many=True).data
        context['about'] = serializers.AboutSerializer(ToolBoxModels.About.objects.all(), many=True).data
        context['about'][0]['body'] = md.convert(context['about'][0]['body'])
        context['about'][0]['created_time'] = context['about'][0]['created_time'][0:10]
        return Response(context)

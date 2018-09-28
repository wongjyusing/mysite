from rest_framework import serializers

from .blog import models as BlogModels
from .toolbox import models as ToolBoxModels

# 博客部分序列化
class BlogListTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModels.BlogTag
        fields = ('name','slug')

class BlogListSerializer(serializers.ModelSerializer):
    blog_tag = BlogListTagSerializer(many=True)
    class Meta:
        model = BlogModels.Blog
        fields = ('title', 'slug', 'author', 'created_time', 'update_time','blog_tag')



class BlogDeatilSerializer(serializers.ModelSerializer):
    blog_tag = BlogListTagSerializer(many=True)


    class Meta:
        model = BlogModels.Blog
        fields = ('__all__')

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModels.BlogTag
        fields = ('name','slug','body')


# 通用工具部分序列化
class GitBookLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBoxModels.GitBookLink
        fields = ('name', 'link','book_status')

class SiteDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBoxModels.MySiteData
        fields = ('logo', 'introduction', 'source_of_power','approval_number')






class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBoxModels.Home
        fields = ('title', 'author', 'created_time','update_time','body')

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBoxModels.About
        fields = ('title', 'author', 'created_time','update_time','body')



class FriendLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBoxModels.FriendLink
        fields = ('name', 'link')

class SpaceLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBoxModels.SpaceLink
        fields = ('name', 'link')

class BookLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBoxModels.BookLink
        fields = ('name', 'link')

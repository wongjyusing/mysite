from rest_framework import serializers

from .blog import models as BlogModels

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
        fields = ('title', 'slug', 'author','body', 'created_time', 'update_time','blog_tag')

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModels.BlogTag
        fields = ('name','slug','body')

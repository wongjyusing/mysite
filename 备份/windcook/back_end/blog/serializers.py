from rest_framework import serializers
from .models import Blog,BlogTag
'''
class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = '__all__'
'''
class BlogListSerializer(serializers.ModelSerializer):
    blog_tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        fields = '__all__'

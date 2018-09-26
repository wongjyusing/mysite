from rest_framework import serializers
from .blog import models as BlogModel

class BlogList(serializers.ModelSerializer):

    blog_tag = serializers.StringRelatedField(many=True)
    class Meta:
        model = BlogModel.Blog
        fields = '__all__'



class BlogTagSerializer(serializers.ModelSerializer):
    card = BlogList(many=True)
    class Meta:
        model = BlogModel.BlogTag
        fields = '__all__'




class BlogListTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel.BlogTag
        fields = '__all__'





class BlogListSerializer(serializers.ModelSerializer):

    #blog_tag = serializers.StringRelatedField(many=True)
    blog_tag = BlogListTagSerializer(many=True)
    class Meta:
        model = BlogModel.Blog
        fields = '__all__'

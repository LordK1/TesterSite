from rest_framework import serializers
from post.models import Category, Post

__author__ = 'k1'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'created_date', 'updated_date']


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['title', 'posts', 'created_date']

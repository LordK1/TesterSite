from rest_framework import serializers
from post.models import Category, Post

__author__ = 'k1'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'created_date']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'created_date', 'updated_date']

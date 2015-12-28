from rest_framework import serializers
from post.models import Category, Post

__author__ = 'k1'


class PostSerializer(serializers.ModelSerializer):
    # category = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='category-detail')

    class Meta:
        model = Post
        fields = ['title', 'created_date', 'updated_date']


class CategorySerializer(serializers.ModelSerializer):
    # posts = serializers.StringRelatedField(many=True)
    # posts = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='post-detail')
    posts = PostSerializer(many=True, read_only=True)

    def create(self, validated_data):
        posts_data = validated_data.pop('posts')
        category = Category.objects.create(**validated_data)
        for post_data in posts_data:
            Post.objects.create(category=category, **post_data)
        return category

    class Meta:
        model = Category
        fields = ['title', 'posts', 'created_date']

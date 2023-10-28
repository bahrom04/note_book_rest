from django.contrib.auth.models import User, Group
from rest_framework import serializers
from home1.models import Posts, Categories, Authors, ResentlyPosteds, Popular, Featured, TopAuthors, TodaysUpdates


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['category', 'author', 'title', 'image', 'published_at', 'time_to_read', 'description']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['title']


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['name']




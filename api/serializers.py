from rest_framework import serializers
from .models import Task, Category, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data);
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user_profile', 'img']
        extra_kwargs = {'user_profile': {'read_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'item']


class TaskSerializer(serializers.ModelSerializer):
    category_item = serializers.ReadOnlyField(source='category.item', read_only=True)
    owner_name = serializers.ReadOnlyField(source='owner.username', read_only=True)
    responsible_name = serializers.ReadOnlyField(source='responsible.username', read_only=True)
    status_name = serializers.CharField(source='get_status_display', read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'criteria', 'status', 'status_name', 'category', 'category_item',
                  'estimate', 'responsible_name', 'owner_name', 'responsible', 'owner', 'created_at', 'updated_at']
        extra_kwargs = {'owner': {'read_only': True}}
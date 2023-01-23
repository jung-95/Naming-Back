from rest_framework import serializers
from .models import *

class dictionarySerializer(serializers.ModelSerializer):
    firstName = serializers.SerializerMethodField()
    def get_firstName(self, obj):
        return obj.firstName

    class Meta:
        model = dictionary
        fields = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border']

class postSerializer(serializers.ModelSerializer):
    is_liked = serializers.BooleanField(default=False)
    like = serializers.IntegerField(default=0)
    stack = serializers.IntegerField(default=0)

    class Meta:
        model = post
        fields = ['id', 'consonant', 'contents', 'like', 'is_liked', 'stack']

class dictionaryListSerializer(serializers.ModelSerializer):
    stacked = postSerializer(many = True, read_only = True)
    firstName = serializers.SerializerMethodField()
    def get_firstName(self, obj):
        return obj.firstName

    class Meta:
        model = dictionary
        fields = ['id', 'userId', 'firstName', 'color', 'shadow', 'shadowColor', 'border', 'stacked']

class dictionaryPostSerializer(serializers.ModelSerializer):
    post = postSerializer(many = True, read_only = True)
    class Meta:
        model = dictionary
        fields = ['id', 'post']

class NickNameSerializer(serializers.ModelSerializer):
    people = serializers.IntegerField(default=0)

    class Meta:
        model = post
        fields = ['id', 'nickname', 'people']
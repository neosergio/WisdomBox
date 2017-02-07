from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Card


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('username', 'first_name', 'last_name', 'is_staff', 'is_active', 'email')


class CardSerializer(serializers.ModelSerializer):

    created_by = UserSimpleSerializer()
    updated_by = UserSimpleSerializer()

    class Meta(object):
        model = Card
        fields = '__all__'
        depth = 1

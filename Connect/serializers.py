# app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DoorClick

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class DoorClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorClick
        fields = ['timestamp']

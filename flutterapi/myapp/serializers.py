#ระบุการโชว์ข้อมูล

from django.db.models.base import Model
from rest_framework import serializers
from .models import Todolist

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id','title','detail') #'__all__'

from rest_framework import serializers
from .models import TodoDetails,tag

class tagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields =['tag_name']

class TodoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TodoDetails
        fields = '__all__'


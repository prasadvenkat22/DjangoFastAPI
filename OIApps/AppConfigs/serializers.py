from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,ReadOnlyField
from .models import App,Category,Scope
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class AppSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = App
        fields = ('__all__')
class CategorySerializer(serializers.ModelSerializer):
    Apps = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Applicaitons = serializers.SlugRelatedField(
    #                     many=True, 
    #                     read_only=True,
    #                     slug_field="name"
    #                             )                         
    class Meta:
        model = Category
        fields = ('__all__')
class ScopeSerializer(serializers.ModelSerializer):
    Categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Scope
        fields = ('__all__')

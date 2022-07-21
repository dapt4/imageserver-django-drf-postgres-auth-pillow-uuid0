from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Img

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    class Meta:
        model = Img
        fields = ['id', 'url', 'user']

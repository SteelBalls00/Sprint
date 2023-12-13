from .models import *
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['name', 'email', 'phone']



class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['summer', 'autumn', 'winter', 'spring']


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.URLField()
    class Meta:
        model = Images
        fields = ['title', 'date_added', 'image']


class PerevalsSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coord = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImagesSerializer(many=True, required=False)

    class Meta:
        model = Perevals
        fields = ['beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status', 'level', 'user', 'coord', 'images']




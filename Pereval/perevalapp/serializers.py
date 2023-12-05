from rest_framework import serializers
from .models import PerevalAdd, Coord, Users, Level, Images
from drf_writable_nested import WritableNestedModelSerializer



class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    data = serializers.URLField()
    class Meta:
        model = Images
        fields = '__all__'

class PerevalSerializer(WritableNestedModelSerializer):
    user = UsersSerializer()
    coords = CoordSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)
    class Meta:
        model = PerevalAdd
        fields = ['id', 'images', 'user', 'coords', 'level', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'coords_id', 'level_diff', 'user_id']






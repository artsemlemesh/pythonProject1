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
        fields = ['data', 'title']

class PerevalSerializer(WritableNestedModelSerializer):
    user_id = UsersSerializer()
    coords_id = CoordSerializer()
    level_diff = LevelSerializer(allow_null=True)
    image = ImageSerializer(many=True)
    class Meta:
        model = PerevalAdd
        fields = ['id', 'user_id', 'coords_id', 'level_diff', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'image', 'status']   #'id', 'images', 'user', 'coords', 'level', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time'




    def validate(self, data):
        if self.instance is not None:
            user_instance = self.instance.user_id
            user_data = data.get('user_id')
            valid_user_fields = [
                user_instance.email != user_data['email'],
                user_instance.full_name != user_data['full_name'],
                user_instance.phone != user_data['phone']
            ]
            if user_data and any(valid_user_fields):
                raise serializers.ValidationError({'cant be changed'})
        return data



    # def create(self, validated_data, **kwargs):
    #     user_id = validated_data.pop('user_id')
    #     coords_id = validated_data.pop('coords_id')
    #     level_diff = validated_data.pop('level_diff')
    #     images = validated_data.pop('image')
    #
    #     unique_user = Users.objects.filter(email=user_id['email'])
    #     if unique_user.exists():
    #         user_serializer = UsersSerializer(data=user_id)
    #         user_serializer.is_valid(raise_exception=True)
    #         user_id = user_serializer.save()
    #     else:
    #         user_id = Users.objects.create(**user_id)
    #
    #     coords_id = Coord.objects.create(**coords_id)
    #     level_diff = Level.objects.create(**level_diff)
    #     pereval_id = PerevalAdd.objects.create(**validated_data, user_id=user_id, coords_id=coords_id, level_diff=level_diff, status='new')
    #
    #     for image in images:
    #         data = image.pop('data')
    #         title = image.pop('title')
    #         Images.objects.create(data = data, title=title, pereval_id=pereval_id)
    #
    #     return pereval_id







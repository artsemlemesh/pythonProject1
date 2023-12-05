from rest_framework import serializers
from .models import PerevalAdd, Coord, Users, Level



class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdd
        fields = ['id', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'coords_id', 'level_diff', 'user_id']






# class PerevalSerializer(serializers.Serializer):
#     beauty_title = serializers.CharField()
#     title = serializers.CharField()
#     other_titles = serializers.CharField()
#     connect = serializers.CharField()
#     add_time = serializers.DateTimeField(read_only=True)
#     user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
#     coords_id = serializers.PrimaryKeyRelatedField(queryset=Coord.objects.all())
#     level_diff = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all())
#
#
#     class Meta:
#         model = PerevalAdd
#         fields = ['pk', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'user_id', 'coords_id', 'level_diff'] # 'user_id', 'coords_id', 'level_diff'
#
#
#     def create(self, validated_data):
#         return PerevalAdd.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
#         instance.title = validated_data.get('title', instance.title)
#         instance.other_titles = validated_data.get('other_titles', instance.other_titles)
#         instance.connect = validated_data.get('connect', instance.connect)
#         instance.add_time = validated_data.get('add_time', instance.add_time)
#         instance.user_id = validated_data.get('user_id', instance.user_id)
#         instance.coords_id = validated_data.get('coords_id', instance.coords_id)
#         instance.level_diff = validated_data.get('level_diff', instance.level_diff)
#         instance.save()
#         return instance
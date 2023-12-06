from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import *
from .models import PerevalAdd, Coord, Level, Users, Images
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer



class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         return PerevalAdd.objects.all()[:3]
    #
    #     return PerevalAdd.objects.filter(pk=pk)
    #
    #
    # @action(methods=['get'], detail=True)
    # def users(self, request, pk=None):
    #     user = Users.objects.get(pk=pk)
    #     return Response({'users': [user.email]})






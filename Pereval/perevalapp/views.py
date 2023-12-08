
from rest_framework import  viewsets
from .serializers import *
from .models import PerevalAdd, Coord, Level, Users, Images
from rest_framework.response import Response
from rest_framework import status


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


    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED, 'message': 'Success', 'id': serializer.data['id']})
        else:
            errors = serializer.errors
            error_status = status.HTTP_400_BAD_REQUEST if errors else status.HTTP_500_INTERNAL_SERVER_ERROR
            error_message = 'failed to process the data' if errors else 'server\'s error'
            return Response({'status': error_status, 'message': error_message, 'errors': errors, 'id': None})

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






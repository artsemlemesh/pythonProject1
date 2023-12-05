from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import PerevalSerializer
from .models import PerevalAdd, Coord, Level, Users
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action

class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return PerevalAdd.objects.all()[:3]

        return PerevalAdd.objects.filter(pk=pk)


    @action(methods=['get'], detail=True)
    def users(self, request, pk=None):
        user = Users.objects.get(pk=pk)
        return Response({'users': [user.email]})



class PerevalAPIList(generics.ListCreateAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer

class PerevalAPIUpdate(generics.UpdateAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer

class PerevalAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer







class PerevalAPI(APIView):
    def get(self, request):
        lst = PerevalAdd.objects.all().values()
        return Response({'posts': PerevalSerializer(lst, many=True).data})

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed, pk has not been found'})

        try:
            instance = PerevalAdd.objects.get(pk=pk)
        except:
            return Response({'error': 'objects does not exist'})

        serializer = PerevalSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DeletE not allowed'})
        try:
            instance = PerevalAdd.objects.get(pk=pk)
        except PerevalAdd.DoesNotExist:
            return Response({'error': 'obj Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response({'success': f'post: {pk} deleted'} ,status=status.HTTP_204_NO_CONTENT)




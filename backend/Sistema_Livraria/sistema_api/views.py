from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Autor, Livro, Editora
from .serializers import AutorSerializer, LivroSerializer, EditoraSerializer

class EditoraListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        
        autores = Editora.objects.all()
        serializer = EditoraSerializer(autores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'Nome_Editora': request.data.get('Nome_Editora'), 
            'Cnpj': request.data.get('Cnpj'), 
        }
        serializer = EditoraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.




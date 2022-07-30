from email import message
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializer
from rest_framework import viewsets

# Create your views here.

class HelloApiView(APIView):
    """API View de prueba"""
    serializer_class = serializer.HelloSerializers

    def get(self, request, format=None):
        """Retornar listas de caracteristicas de APIView"""
        an_apiview =[
            'Usamos metodos HTTP como funciones(get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django'
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los urls',
        ]

        return Response({'message': 'Hello', 'an_apivier': an_apiview})

    def post(self,request):
        """crea un mensaje con nuestro numbre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put (self, request, pk=None):
        """Maneja actualizar un objeto"""
        return Response({'method': 'PUT'})

    def patch (self, request, pk=None):
        """Maneja actualizacion parcial de un objeto"""
        return Response({'method': 'PATCH'})

    def delete (self, request, pk=None):
        """Maneja borrar un objeto"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test Api view set"""
    serializer_class = serializer.HelloSerializers    

    def list(self, request):
        """retornar mensaje de hola mundo"""

        a_viewset = [
            'Usa acciones (ist, create, retrieve, update, partial_update',
            'automatiacamente mapea a los URLs usando RRouters',
            'Provee mas funciolaidad con menos codigo'
        ]

        return Response({'message': 'hola', 'a_viewset': a_viewset})

    def create(self , request):
        """crear nuevo mensaje hola mundo"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hola {name}"
            return Response ({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""

        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """actualiza un objeto"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """actualiza parcialmente un objeto"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """destruye un objeto"""

        return Response({'http_method': 'DELETE'})

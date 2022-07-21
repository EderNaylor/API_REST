from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """API View de prueba"""

    def get(self, request, format=None):
        """Retornar listas de caracteristicas de APIView"""
        an_apiview =[
            'Usamos metodos HTTP como funciones(get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django'
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los urls',
        ]

        return Response({'message': 'Hello', 'an_apivier': an_apiview})

from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Serializar nuestro campo para probar nuestro APIView"""
    name = serializers.CharField(max_length=10)

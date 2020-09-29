from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialize a name field for test API"""
    name = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    

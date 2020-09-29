from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers



class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        apiview_list = [
            'Test API',
            'Test API2',
            'Test API3',
        ]

        return Response({'message': 'Hello!', 'results': apiview_list})

    def post(self, request):
        """Create a Hello message for a user"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.data.get('email')
            message = f'Hello {name}'
            return Response({'message': message, 'email': email})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        return Response({'method': 'PUT'})

    def patch(self, request):
        return Response({'method': 'PATCH'})

    def delete(self, request):
        return Response({'method': 'DELETE'})
        

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions



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
        

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""
        a_viewset = [
            'test1',
            'test2',
            'test3',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'method': 'GET'})

    def update(self, request, pk):
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk):
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk):
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UserProfilePermission,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('name', 'email')
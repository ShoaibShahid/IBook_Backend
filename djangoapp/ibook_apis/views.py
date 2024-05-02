from django.shortcuts import render, HttpResponse
from .serializers import  CreateUserSerializer,LoginUserSerializer, ProjectSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets, status
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import ProjectModel
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CreateUserSerializer

class LoginUserView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginUserSerializer

class ProjectCreateView(generics.CreateAPIView):
    queryset = ProjectModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializer

@api_view(['POST'])
def getUserProjectsView(request):
    # Check if the request has a user_id in the POST data
    if 'user_id' not in request.data:
        return Response({'error': 'User ID is required in the request body'}, status=status.HTTP_400_BAD_REQUEST)

    user_id = request.data['user_id']

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Get all products associated with the user
    projects = ProjectModel.objects.filter(user=user)

    # Serialize the products
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)

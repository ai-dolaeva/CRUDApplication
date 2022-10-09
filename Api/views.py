from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from Api.serializers import UserSerializer
from Api.models import User
from Api.permissions import IsOwnerOrAdminOrReadOnly

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for data manipulation
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view
        requires.
        """
        if self.action in ['retrieve', 'list', 'create']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]
        return [permission() for permission in permission_classes]
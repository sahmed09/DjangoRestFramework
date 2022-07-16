from gallery.models import *
from gallery.api.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class AlbumModelViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class AlbumItemsModelViewSet(viewsets.ModelViewSet):
    queryset = AlbumItems.objects.all()
    serializer_class = AlbumItemsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['album__name']

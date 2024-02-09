from messenger.models import *
from messenger.api.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class ConversationModelViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']


class ConversationMemberModelViewSet(viewsets.ModelViewSet):
    queryset = ConversationMember.objects.all()
    serializer_class = ConversationMemberSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['conversation__name']


class MessageModelViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['conversation__name']


class MessageSeenStatusModelViewSet(viewsets.ModelViewSet):
    queryset = MessageSeenStatus.objects.all()
    serializer_class = MessageSeenStatusSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

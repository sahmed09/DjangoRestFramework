from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.models import User
from messenger.models import *


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'


class ConversationMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMember
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('conversation'):
            self.fields['conversation'] = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())

            con_name = data['conversation']['name']
            conv = get_object_or_404(Conversation, name=con_name)

            data['conversation'] = conv.id

        if data.get('user'):
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

            username = data['user']['username']
            user = get_object_or_404(User, username=username)

            data['user'] = user.id

        return super(ConversationMemberSerializer, self).to_internal_value(data)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('user'):
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

            username = data['user']['username']
            user = get_object_or_404(User, username=username)

            data['user'] = user.id

        if data.get('conversation'):
            self.fields['conversation'] = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())

            con_name = data['conversation']['name']
            conv = get_object_or_404(Conversation, name=con_name)

            data['conversation'] = conv.id

        return super(MessageSerializer, self).to_internal_value(data)


class MessageSeenStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageSeenStatus
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('conversation'):
            self.fields['conversation'] = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())

            con_name = data['conversation']['name']
            conv = get_object_or_404(Conversation, name=con_name)

            data['conversation'] = conv.id

        if data.get('user'):
            self.fields['user'] = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

            username = data['user']['username']
            user = get_object_or_404(User, username=username)

            data['user'] = user.id

        return super(MessageSeenStatusSerializer, self).to_internal_value(data)

from django.contrib import admin
from .models import *

admin.site.register(Conversation)
admin.site.register(ConversationMember)
admin.site.register(Message)
admin.site.register(MessageSeenStatus)

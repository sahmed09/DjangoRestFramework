from django.urls import path, include
from messenger.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('conversation_api', views.ConversationModelViewSet, basename='conversation')
router.register('conversation_member_api', views.ConversationMemberModelViewSet, basename='conversation_member')
router.register('message_api', views.MessageModelViewSet, basename='message')
router.register('message_seen_status_api', views.MessageSeenStatusModelViewSet, basename='message_seen_status')

app_name = 'messenger'
urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from gallery.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('album_api', views.AlbumModelViewSet, basename='album')
router.register('album_items_api', views.AlbumItemsModelViewSet, basename='album_items')

app_name = 'gallery'
urlpatterns = [
    path('', include(router.urls)),
]

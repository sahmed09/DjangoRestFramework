from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# APIs using ViewSets
router = DefaultRouter()
router.register('students', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

"""
# General Class Based APIs using APIView + APIs using Mixins + APIs using Generic Views
urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
]
"""

from django.urls import path, include
from accounting.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('transaction_graph_api', views.TransactionGraphListViewSet, basename='transaction_graph')

app_name = 'accounting'
urlpatterns = [
    path('', include(router.urls)),
]

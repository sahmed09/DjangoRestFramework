from django.urls import path, include
from order.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user_api', views.UserListViewSet, basename='user')
router.register('customer_api', views.CustomerModelViewSet, basename='customer')
router.register('area_api', views.AreaModelViewSet, basename='area')
router.register('delivery_agency_api', views.DeliveryAgencyModelViewSet, basename='delivery_agency')
router.register('shop_order_status_api', views.ShopOrderStatusModelViewSet, basename='shop_order_status')
router.register('order_status_api', views.OrderStatusModelViewSet, basename='order_status')
router.register('order_api', views.OrderModelViewSet, basename='order')
router.register('order_item_api', views.OrderItemModelViewSet, basename='order_item')
router.register('delivery_agency_orders_api', views.DeliveryAgencyOrdersModelViewSet, basename='delivery_agency_orders')

app_name = 'order'
urlpatterns = [
    path('', include(router.urls)),
]

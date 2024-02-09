from django.urls import path, include
from shop.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('shop_api', views.ShopModelViewSet, basename='shop')
router.register('shop_role_api', views.ShopRoleModelViewSet, basename='shop_role')
router.register('shop_branch_api', views.ShopBranchModelViewSet, basename='shop_branch')
router.register('shop_branch_product_api', views.ShopBranchProductModelViewSet, basename='shop_branch_product')
router.register('stock_api', views.StockModelViewSet, basename='stock')
router.register('stock_alerts_api', views.StockAlertsModelViewSet, basename='stock_alerts')
router.register('stock_alert_group_api', views.StockAlertGroupModelViewSet, basename='stock_alert_group')
router.register('stock_alert_subscription_api', views.StockAlertSubscriptionModelViewSet,
                basename='stock_alert_subscription')
router.register('stock_alert_group_subscription_api', views.StockAlertGroupSubscriptionModelViewSet,
                basename='stock_alert_group_subscription')
router.register('product_stock_log_api', views.ProductStockLogListViewSet, basename='product_stock_log')

app_name = 'shop'
urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
from store.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category_api', views.CategoryModelViewSet, basename='category')
router.register('brand_api', views.BrandModelViewSet, basename='brand')
router.register('product_api', views.ProductModelViewSet, basename='product')
router.register('variation_api', views.VariationModelViewSet, basename='variation')
router.register('product_variations_api', views.ProductVariationsModelViewSet, basename='product_variations')
router.register('category_attribute_api', views.CategoryAttributesModelViewSet, basename='category_attribute')
router.register('variation_category_attributes_api', views.VariationCategoryAttributesModelViewSet,
                basename='variation_category_attributes')
router.register('category_attribute_choices_api', views.CategoryAttributeChoicesModelViewSet,
                basename='category_attribute_choices')
router.register('product_category_attribute_choices_api', views.ProductCategoryAttributeChoicesModelViewSet,
                basename='product_category_attribute_choices')
router.register('product_attributes_api', views.ProductAttributesModelViewSet, basename='product_attributes')
router.register('product_list', views.ProductFilterListViewSet, basename='product_list')

app_name = 'store'
urlpatterns = [
    path('', include(router.urls)),
]

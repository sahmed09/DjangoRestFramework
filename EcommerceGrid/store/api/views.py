from rest_framework import mixins
from rest_framework.response import Response
from store.models import *
from store.api.serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['slug']


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['slug']


class VariationModelViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter]
    search_fields = ['name']


class ProductVariationsModelViewSet(viewsets.ModelViewSet):
    queryset = ProductVariations.objects.all()
    serializer_class = ProductVariationsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CategoryAttributesModelViewSet(viewsets.ModelViewSet):
    queryset = CategoryAttributes.objects.all()
    serializer_class = CategoryAttributesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category__slug']


class VariationCategoryAttributesModelViewSet(viewsets.ModelViewSet):
    queryset = VariationCategoryAttributes.objects.all()
    serializer_class = VariationCategoryAttributesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class CategoryAttributeChoicesModelViewSet(viewsets.ModelViewSet):
    queryset = CategoryAttributeChoices.objects.all()
    serializer_class = CategoryAttributeChoicesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # filter_backends = [SearchFilter]
    # search_fields = ['category_attribute__slug']
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category_attribute__slug']


class ProductCategoryAttributeChoicesModelViewSet(viewsets.ModelViewSet):
    queryset = ProductCategoryAttributeChoices.objects.all()
    serializer_class = ProductCategoryAttributeChoicesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['product__slug']


class ProductFilterListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['category__slug']

    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductFilterListViewSet, self).get_queryset()

        for category_attribute in self.request.query_params.keys():
            if category_attribute not in self.filter_fields:
                attribute_choices = self.request.query_params.getlist(category_attribute)

                for attribute_choice in attribute_choices:
                    queryset = queryset.filter(
                        productcategoryattributechoices__category_attribute_choices__slug=attribute_choice).filter(
                        productcategoryattributechoices__category_attribute_choices__category_attribute__slug=category_attribute)

        return queryset.distinct()


class ProductAttributesModelViewSet(viewsets.ModelViewSet):
    queryset = ProductCategoryAttributeChoices.objects.all()
    serializer_class = ProductCategoryAttributeChoicesSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['product__slug']

    def create(self, request, *args, **kwargs):
        p_slug = request.query_params.get('product__slug')

        message = {}

        for data in request.data['data']:
            cac = ProductCategoryAttributeChoices.objects.filter(product__slug=p_slug,
                                                                 category_attribute_choices__category_attribute__slug=
                                                                 data['category_attribute']['slug']).first()

            if cac is None:
                ProductCategoryAttributeChoices.objects.create(product=Product.objects.filter(slug=p_slug).first(),
                                                               category_attribute_choices=CategoryAttributeChoices.objects.filter(
                                                                   category_attribute__slug=data['category_attribute'][
                                                                       'slug'], slug=data['category_attribute_choices'][
                                                                       'slug']).first())
                message = {"message": "Product Category attribute choices added"}

            elif cac.category_attribute_choices.slug != data['category_attribute_choices']['slug']:
                cac.category_attribute_choices = CategoryAttributeChoices.objects.filter(
                    category_attribute__slug=data['category_attribute']['slug'],
                    slug=data['category_attribute_choices']['slug']).first()
                cac.save()
                message = {"message": "Product Category attribute choices updated"}
        return Response(message)

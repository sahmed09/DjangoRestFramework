from rest_framework import serializers
from store.models import *
from gallery.models import Album
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['slug']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ['slug']

    def to_internal_value(self, data):
        if data.get('album'):
            self.fields['album'] = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

            album_name = data['album']['name']
            album = get_object_or_404(Album, name=album_name)

            data['album'] = album.id

        return super(BrandSerializer, self).to_internal_value(data)


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = '__all__'


class ProductSerializerSummary(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'slug']


class ProductVariationsSerializer(serializers.ModelSerializer):
    product = ProductSerializerSummary()

    class Meta:
        model = ProductVariations
        fields = ['product']

    def to_internal_value(self, data):
        if data.get('product'):
            self.fields['product'] = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

            product_slug = data['product']['slug']
            product = get_object_or_404(Product, slug=product_slug)

            data['product'] = product.id

        return super(ProductVariationsSerializer, self).to_internal_value(data)


class CategoryAttributesSerializerSummary(serializers.ModelSerializer):
    class Meta:
        model = CategoryAttributes
        fields = ['attribute_name', 'slug']


class VariationCategoryAttributesSerializer(serializers.ModelSerializer):
    category_attribute = CategoryAttributesSerializerSummary()

    class Meta:
        model = VariationCategoryAttributes
        fields = ['category_attribute', 'variation']

    def to_internal_value(self, data):
        if data.get('category_attribute'):
            self.fields['category_attribute'] = serializers.PrimaryKeyRelatedField(
                queryset=CategoryAttributes.objects.all())

            cat_attr_slug = data['category_attribute']['slug']
            cat_attr = get_object_or_404(CategoryAttributes, slug=cat_attr_slug)

            data['category_attribute'] = cat_attr.id

        return super(VariationCategoryAttributesSerializer, self).to_internal_value(data)


class CategoryAttributesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = CategoryAttributes
        fields = ['category', 'attribute_name', 'slug', 'id']
        read_only_fields = ['slug']

    def to_internal_value(self, data):
        if data.get('category'):
            self.fields['category'] = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

            cat_slug = data['category']['slug']
            cat = get_object_or_404(Category, slug=cat_slug)

            data['category'] = cat.id

        return super(CategoryAttributesSerializer, self).to_internal_value(data)


class CategoryAttributeChoicesSerializer(serializers.ModelSerializer):
    category_attribute = CategoryAttributesSerializerSummary()

    class Meta:
        model = CategoryAttributeChoices
        fields = '__all__'
        read_only_fields = ['slug']

    def to_internal_value(self, data):
        if data.get('category_attribute'):
            self.fields['category_attribute'] = serializers.PrimaryKeyRelatedField(
                queryset=CategoryAttributes.objects.all())

            cat_attr_slug = data['category_attribute']['slug']
            cat_attr = get_object_or_404(CategoryAttributes, slug=cat_attr_slug)

            data['category_attribute'] = cat_attr.id

        return super(CategoryAttributeChoicesSerializer, self).to_internal_value(data)


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    variations = ProductVariationsSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'brand', 'album', 'slug', 'variations']
        read_only_fields = ['slug', 'variations']

    def to_internal_value(self, data):
        if data.get('category'):
            self.fields['category'] = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

            cat_slug = data['category']['slug']
            cat = get_object_or_404(Category, slug=cat_slug)

            data['category'] = cat.id

        if data.get('brand'):
            self.fields['brand'] = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
            brand_slug = data['brand']['slug']
            brand = get_object_or_404(Brand, slug=brand_slug)

            data['brand'] = brand.id

        if data.get('album'):
            self.fields['album'] = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

            album_name = data['album']['name']
            album = get_object_or_404(Album, name=album_name)

            data['album'] = album.id

        return super(ProductSerializer, self).to_internal_value(data)


class ProductCategoryAttributeChoicesSerializer(serializers.ModelSerializer):
    product = ProductSerializerSummary()
    category_attribute_choices = CategoryAttributeChoicesSerializer()

    class Meta:
        model = ProductCategoryAttributeChoices
        fields = '__all__'

    def to_internal_value(self, data):
        if data.get('product'):
            self.fields['product'] = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

            product_slug = data['product']['slug']
            product = get_object_or_404(Product, slug=product_slug)

            data['product'] = product.id

        if data.get('category_attribute_choices'):
            self.fields['category_attribute_choices'] = serializers.PrimaryKeyRelatedField(
                queryset=CategoryAttributeChoices.objects.all())

            cat_attr_choices_slug = data['category_attribute_choices']['slug']
            cat_attr_choices = get_object_or_404(CategoryAttributeChoices, slug=cat_attr_choices_slug)

            data['category_attribute_choices'] = cat_attr_choices.id

        return super(ProductCategoryAttributeChoicesSerializer, self).to_internal_value(data)

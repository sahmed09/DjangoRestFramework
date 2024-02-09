from django.contrib import admin
from .models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(CategoryAttributes)
# admin.site.register(CategoryAttributeChoices)
# admin.site.register(ProductCategoryAttributeChoices)


class CategoryAttributeChoicesInline(NestedStackedInline):
    model = CategoryAttributeChoices
    extra = 1
    fk_name = 'category_attribute'


class CategoryAttributesInline(NestedStackedInline):
    model = CategoryAttributes
    extra = 1
    fk_name = 'category'
    inlines = [CategoryAttributeChoicesInline]


class CategoryAdmin(NestedModelAdmin):
    model = Category
    extra = 1
    inlines = [CategoryAttributesInline]


admin.site.register(Category, CategoryAdmin)

admin.site.register(Brand)


class ProductCategoryAttributeChoicesInline(admin.TabularInline):
    model = ProductCategoryAttributeChoices


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    inlines = [ProductCategoryAttributeChoicesInline]


admin.site.register(Product, ProductAdmin)

admin.site.register(Variation)
admin.site.register(ProductVariations)
admin.site.register(VariationCategoryAttributes)

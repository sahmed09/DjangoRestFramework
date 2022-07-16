from django.db import models
from django.utils.text import slugify


def unique_slug(mdl, target_name):
    slug = slugify(target_name)

    check_slug = mdl.objects.filter(slug=slug).exists()
    count = 1
    while check_slug:
        count += 1
        slug = slugify(target_name) + '-' + str(count)
        check_slug = mdl.objects.filter(slug=slug).exists()
    return slug


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(Category, self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)
    album = models.ForeignKey('gallery.Album', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(Brand, self.name)
        super(Brand, self).save(*args, **kwargs)


class Variation(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)
    album = models.ForeignKey('gallery.Album', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(Product, self.name)
        super(Product, self).save(*args, **kwargs)


class ProductVariations(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variations')
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} - {self.variation}'

    class Meta:
        verbose_name_plural = "Product Variations"


class CategoryAttributes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.attribute_name}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(CategoryAttributes, self.attribute_name)
        super(CategoryAttributes, self).save(*args, **kwargs)


class VariationCategoryAttributes(models.Model):
    category_attribute = models.ForeignKey(CategoryAttributes, on_delete=models.CASCADE,
                                           related_name='category_attribute_variations')
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.variation} - {self.category_attribute}'

    class Meta:
        verbose_name_plural = "Variation Category Attributes"


class CategoryAttributeChoices(models.Model):
    category_attribute = models.ForeignKey(CategoryAttributes, on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.attribute_value}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = unique_slug(CategoryAttributeChoices, self.attribute_value)
        super(CategoryAttributeChoices, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Category Attribute Choices"


class ProductCategoryAttributeChoices(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_attribute_choices = models.ForeignKey(CategoryAttributeChoices, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name_plural = "Product Category Attribute Choices"

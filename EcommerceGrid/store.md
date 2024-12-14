## Store APIs
```
http://54.251.167.179:8000/api/store/
```

### Category API: 
http://54.251.167.179:8000/api/store/category_api/ <br>
Required fields: name <br>
Example:
```json
{
    "name": "Mouse"
}
```
Output:
```
{
    "id": 2,
    "name": "Mouse",
    "slug": "mouse"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/store/category_api/?search=mouse
Output:
{
    "id": 2,
    "name": "Mouse",
    "slug": "mouse"
}
```

### Brand API: 
http://54.251.167.179:8000/api/store/brand_api/ <br>
Required fields: name <br>
Optional Field: album <br>
Example:
```
{
    "name": "Acer",
    "album": {"name": "album_name"}
}
```
Output:
```
{
    "id": 1,
    "name": "Singer",
    "slug": "singer",
    "album": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/store/brand_api/?search=singer
Output:
{
    "id": 1,
    "name": "Singer",
    "slug": "singer",
    "album": 1
}
```

### Variation API: 
http://54.251.167.179:8000/api/store/variation_api/
```
Just Send POST request
```

### Product API: 
http://54.251.167.179:8000/api/store/product_api/ <br>
Required fields: category, brand, name <br>
Optional Field: album <br>
Example:
```
{
    "name": "LogiTech Mouse",
    "category": {"slug": "mouse"},
    "brand": {"slug": "acer"},
    "album": {"name": "album_name"}
}
```
Output:
```
{
    "id": 1,
    "name": "LogiTech Mouse",
    "category": {
        "id": 2,
        "name": "Mouse",
        "slug": "mouse"
    },
    "brand": {
        "id": 3,
        "name": "Acer",
        "slug": "acer",
        "album": 1
    },
    "album": 1,
    "slug": "singer-double-door-frost-fridge",
    "variations": []
}
```
Searching Example:
```
http://54.251.167.179:8000/api/store/product_api/?search=Singer Double Door Frost Fridge
Output:
{
    "id": 1,
    "name": "Singer Double Door Frost Fridge",
    "category": {
        "id": 1,
        "name": "Fridge",
        "slug": "fridge"
    },
    "brand": {
        "id": 1,
        "name": "Singer",
        "slug": "singer",
        "album": 1
    },
    "album": 1,
    "slug": "singer-double-door-frost-fridge",
    "variations": [
        {
            "product": {
                "name": "Singer Double Door Frost Fridge",
                "slug": "singer-double-door-frost-fridge"
            }
        }
    ]
}
```

### ProductList Api (For Filtering Products with category, attribute name and attribute value)
http://54.251.167.179:8000/api/store/product_list/ <br>
Filtering Options: category__slug, attribute_name=attribute_value <br>
Filtering Example:
```
http://54.251.167.179:8000/api/store/product_list/?category__slug=fridge&no-of-window=2&frostability=non-frost
Output:
{
    "id": 2,
    "name": "Walton Double Door Non-Frost Fridge",
    "category": {
        "id": 1,
        "name": "Fridge",
        "slug": "fridge"
    },
    "brand": {
        "id": 2,
        "name": "Walton",
        "slug": "walton",
        "album": 1
    },
    "album": 1,
    "slug": "walton-double-door-non-frost-fridge",
    "variations": [
        {
            "product": {
                "name": "Walton Double Door Non-Frost Fridge",
                "slug": "walton-double-door-non-frost-fridge"
            }
        }
    ]
}
```

### ProductVariation API: 
http://54.251.167.179:8000/api/store/product_variations_api/ <br>
Required fields: product, variation <br>
Example:
```
{
    "product": {
        "slug": "walton-double-door-non-frost-fridge"
    },
    "variation": 1
}
```
Output:
```
{
    "product": {
        "name": "Singer Double Door Frost Fridge",
        "slug": "singer-double-door-frost-fridge"
    }
}
```

### CategoryAttribute API: 
http://54.251.167.179:8000/api/store/category_attribute_api/ <br>
Required fields: category, attribute_name <br>
Example:
```
{
    "category": {"slug": "keyboard"},
    "attribute_name": "Total Keys"
}
```
Output:
```
{
    "category": {
        "id": 3,
        "name": "Keyboard",
        "slug": "keyboard"
    },
    "attribute_name": "Total Keys",
    "slug": "total-keys"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/store/category_attribute_api/?category__slug=fridge
Output:
[
    {
        "category": {
            "id": 1,
            "name": "Fridge",
            "slug": "fridge"
        },
        "attribute_name": "No of window",
        "slug": "no-of-window"
    },
    {
        "category": {
            "id": 1,
            "name": "Fridge",
            "slug": "fridge"
        },
        "attribute_name": "Frostability",
        "slug": "frostability"
    }
]
```

### VariationCategoryAttributes API: 
http://54.251.167.179:8000/api/store/variation_category_attributes_api/ <br>
Required fields: <br>
Example:
```
{
    "category_attribute": {"slug": "no-of-window"},
    "variation": 1
}
```
Output:
```
{
    "category_attribute": {
        "attribute_name": "No of window",
        "slug": "no-of-window"
    },
    "variation": 1
}
```

### CategoryAttributeChoices API: 
http://54.251.167.179:8000/api/store/category_attribute_choices_api/ <br>
Required fields: category_attribute, attribute_value <br>
Example:
```
{
    "category_attribute": {"slug": "total-keys"},
    "attribute_value": 106
}
```
Output:
```
{
    "id": 7,
    "category_attribute": {
        "attribute_name": "Total Keys",
        "slug": "total-keys"
    },
    "attribute_value": "106",
    "slug": "106"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/store/category_attribute_choices_api/?category_attribute__slug=total-keys
Output:
[
    {
        "id": 7,
        "category_attribute": {
            "attribute_name": "Total Keys",
            "slug": "total-keys"
        },
        "attribute_value": "106",
        "slug": "106"
    },
    {
        "id": 8,
        "category_attribute": {
            "attribute_name": "Total Keys",
            "slug": "total-keys"
        },
        "attribute_value": "110",
        "slug": "110"
    }
]
```

### ProductCategoryAttributeChoices API: 
http://54.251.167.179:8000/api/store/product_category_attribute_choices_api/ <br>
Required fields: product, category_attribute_choices <br>
Example:
```
{
    "product": {"slug": "walton-double-door-non-frost-fridge"},
    "category_attribute_choices": {"slug": "non-frost"}
}
```
Output:
```
{
    "id": 2,
    "product": {
        "name": "Walton Double Door Non-Frost Fridge",
        "slug": "walton-double-door-non-frost-fridge"
    },
    "category_attribute_choices": {
        "id": 4,
        "category_attribute": {
            "attribute_name": "Frostability",
            "slug": "frostability"
        },
        "attribute_value": "Non-Frost",
        "slug": "non-frost"
    }
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/store/product_category_attribute_choices_api/?product__slug=singer-double-door-frost-fridge
[
    {
        "id": 1,
        "product": {
            "name": "Walton Double Door Non-Frost Fridge",
            "slug": "walton-double-door-non-frost-fridge"
        },
        "category_attribute_choices": {
            "id": 2,
            "category_attribute": {
                "attribute_name": "No of window",
                "slug": "no-of-window"
            },
            "attribute_value": "2",
            "slug": "2"
        }
    },
    {
        "id": 2,
        "product": {
            "name": "Walton Double Door Non-Frost Fridge",
            "slug": "walton-double-door-non-frost-fridge"
        },
        "category_attribute_choices": {
            "id": 4,
            "category_attribute": {
                "attribute_name": "Frostability",
                "slug": "frostability"
            },
            "attribute_value": "Non-Frost",
            "slug": "non-frost"
        }
    }
]
```

### ProductAttributeApi
Add multiple category attribute choices for a specific product. Add product slug with url and send POST 
request with the category attribute name and attribute choice of the product. Will add new attribute if 
the attribute is not present or update the existing value if the attribute is present. <br>

http://54.251.167.179:8000/api/store/product_attributes_api/?product__slug=walton-fridge
```
POST request:
http://54.251.167.179:8000/api/store/product_attributes_api/?product__slug=walton-fridge
{
    "data": [
        {
            "category_attribute": {"slug": "frostability"},
            "category_attribute_choices": {"slug": "non-frost"}
        },
        {
            "category_attribute": {"slug": "no-of-window"},
            "category_attribute_choices": {"slug": "2"}
        }
    ]
}
```

```
Models:
Category: creates category.
Brand: creates brand.
Variation: for creating variations of products or category attributes.
Product: stores product of a specific category and brand.
ProductVariations: Variations of a product.
CategoryAttributes: Creates attributes of a category (like ram, os, battery for a mobile)
VariationCategoryAttributes: Variations of a category attributes.
CategoryAttributeChoices: values of a category attribute (like ram-2gb, ram-4gb, os-ios, os-android)
ProductCategoryAttributeChoices: Add category attribute choices for a product.
```

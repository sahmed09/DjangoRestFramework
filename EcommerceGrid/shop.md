## Shop APIs
```
http://54.251.167.179:8000/api/shop/
```

### Shop API: 
http://54.251.167.179:8000/api/shop/shop_api/ <br>
Required fields: name <br>
Optional Field: album <br>
Example:
```
{
    "name": "Rayans",
    "album": {"name": "album_name"}
}
```
Output:
```
{
    "id": 1,
    "name": "Startech",
    "slug": "startech",
    "album": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/shop/shop_api/?slug=rayans
Output:
{
    "id": 2,
    "name": "Rayans",
    "slug": "rayans",
    "album": 1
}
```

### ShopBranch API: 
http://54.251.167.179:8000/api/shop/shop_branch_api/ <br>
Required fields: shop, name <br>
Optional Field: album <br>
Example:
```
{
    "shop": {"slug": "rayans"},
    "name": "Elephant Road",
}
```
Output:
```
{
    "id": 4,
    "name": "Elephant Road",
    "slug": "rayans-elephant-road",
    "shop": 2,
    "album": null
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/shop/shop_branch_api/?shop__slug=rayans
Output:
[
    {
        "id": 4,
        "name": "Elephant Road",
        "slug": "rayans-elephant-road",
        "shop": 2,
        "album": null
    }
]
```

### ShopBranchProduct API: 
http://54.251.167.179:8000/api/shop/shop_branch_product_api/ <br>
Required fields: shop, product, price <br>
Optional Field: branch <br>
Example:
```
{
    "price": "5000",
    "shop": {"slug": "rayans"},
    "branch": {"slug": "rayans-elephant-road"},
    "product": {"slug": "logitech-mouse"}
}
```
Output:
```
{
    "id": 5,
    "product": {
        "name": "LogiTech Mouse",
        "slug": "logitech-mouse"
    },
    "shop": {
        "name": "Rayans",
        "slug": "rayans"
    },
    "branch": {
        "name": "Elephant Road",
        "slug": "rayans-elephant-road"
    },
    "price": "5000.00"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/shop/shop_branch_product_api/?shop__slug=rayans&branch__slug=&product__slug
Output:
[
    {
        "id": 5,
        "product": {
            "name": "LogiTech Mouse",
            "slug": "logitech-mouse"
        },
        "shop": {
            "name": "Rayans",
            "slug": "rayans"
        },
        "branch": {
            "name": "Elephant Road",
            "slug": "rayans-elephant-road"
        },
        "price": "5000.00"
    }
]
```

### ShopRole API: 
http://54.251.167.179:8000/api/shop/shop_role_api/ <br>
Required fields: user, shop, role <br>
Example:
```
{
    "user": {"username": "admin"},
    "shop": {"slug": "rayans"},
    "role": "SO"
}
```
Output:
```
{
    "id": 2,
    "shop": 2,
    "user": 1,
    "role": "Shop Owner"
}
->
{
    "id": 2,
    "shop": {
        "name": "Rayans",
        "slug": "rayans"
    },
    "user": {
        "username": "admin"
    },
    "role": "Shop Owner"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/shop/shop_role_api/?shop__slug=startech&role=C
Output:
[
    {
        "id": 1,
        "shop": {
            "name": "Startech",
            "slug": "startech"
        },
        "user": {
            "username": "Sakib"
        },
        "role": "Customer"
    }
]
```

### Stock API: 
http://54.251.167.179:8000/api/shop/stock_api/ <br>
Required fields: shop, product, quantity <br>
Optional Field: branch <br>
Example:
```
{
    "quantity": 5,
    "shop": {"slug": "rayans"},
    "branch": {"slug": "rayans-elephant-road"},
    "product": {"slug": "walton-double-door-non-frost-fridge"}
}
```
Output:
```
{
    "id": 1,
    "product": {
        "name": "Walton Double Door Non-Frost Fridge",
        "slug": "walton-double-door-non-frost-fridge"
    },
    "quantity": 7,
    "shop": 2,
    "branch": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/shop/stock_api/?shop__slug=rayans&branch__slug=&product__slug=singer-double-door-frost-fridge
Output:
[
    {
        "id": 3,
        "product": {
            "name": "Singer Double Door Frost Fridge",
            "slug": "singer-double-door-frost-fridge"
        },
        "quantity": 6,
        "shop": 2,
        "branch": 1
    }
]
```

### StockAlerts API: 
http://54.251.167.179:8000/api/shop/stock_alerts_api/ <br>
Required fields: shop, product, name, description, stock_below, stock_above <br>
Optional Field: branch <br>
Example:
```
{
    "shop": {"slug": "rayans"},
    "branch": {"slug": "rayans-elephant-road"},
    "product": {"slug": "singer-double-door-frost-fridge"},
    "name": "Z",
    "description": "z",
    "stock_below": 2,
    "stock_above": 5,
}
```
Output:
```
{
    "id": 3,
    "product": {
        "name": "Singer Double Door Frost Fridge",
        "slug": "singer-double-door-frost-fridge"
    },
    "name": "Z",
    "description": "z",
    "stock_below": 2,
    "stock_above": 5,
    "shop": 2,
    "branch": null
}
```

### StockAlertGroup API: 
http://54.251.167.179:8000/api/shop/stock_alert_group_api/ <br>
Required fields: stock_alert <br>
Example:
```
{
    "stock_alert": {"name": "Z"}
}
```
Output:
```
{
    "id": 3,
    "stock_alert": 3
}
->
{
    "id": 3,
    "stock_alert": {
        "name": "Z",
        "description": "z"
    }
}
```

### StockAlertSubscription API: 
http://54.251.167.179:8000/api/shop/stock_alert_group_api/ <br>
Required fields: user, stock_alert <br>
Example:
```
{
    "user": {"username": "admin"},
    "stock_alert": {"name": "Z"}
}
```
Output:
```
{
    "id": 3,
    "stock_alert": 3,
    "user": 1
}
->
{
    "id": 3,
    "stock_alert": {
        "name": "Z",
        "description": "z"
    },
    "user": {
        "username": "admin"
    }
}
```

### StockAlertGroupSubscription API: 
http://54.251.167.179:8000/api/shop/stock_alert_group_api/ <br>
Required fields: user, stock_alert_group <br>
Example:
```
{
    "user": {"username": "Sakib"},
    "stock_alert_group": 2
}
```
Output:
```
{
    "id": 2,
    "user": 2,
    "stock_alert_group": 2
}
->
{
    "id": 2,
    "user": {
        "username": "Sakib"
    },
    "stock_alert_group": 2
}
```

### ProductStockLog API:
http://54.251.167.179:8000/api/shop/product_stock_log_api/?start_date=2021-10-20&end_date=2022-12-29&interval=daily&product=singer-non-frost-fridge&shop=transcom-digital&branch=banani
<br> Filter Options: start_date, end_date, shop, branch, product, interval (daily, monthly, yearly)
```
Send GET request:
http://54.251.167.179:8000/api/shop/product_stock_log_api/?start_date=2021-10-20&end_date=2022-12-29&interval=daily&product=singer-non-frost-fridge&shop=transcom-digital&branch=banani
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "date": "2021-10-28",
            "max_quantity": 10,
            "min_quantity": 5,
            "avg_quantity": 7.6667
        }
    ]
}
```

```
Models:
Shop: Creates Shop.
ShopBranch: Creates branch for a shop. Branch can be null.
ShopBranchProduct: Add Product in a branch of a shop or in a shop if branch is null.
ShopRole: Creates role for an user in a shop like customer, shop owner, delivery agent, staff etc.
Stock: Add stock of a product in a shop or a shop branch.
    If new stock is added or stock is updated, a signal (update_status) will generated and show current
    stock of the product in a dashboard for a specific shop using websocket for a specifc user like shop owner.
StockAlerts: Create alerts for a specific product of a shop or a shop branch.
StockAlertTrigger: If stock is updated, a trigger is generated by using signal (trigger) if a stock alert is 
    presented for that product.
StockAlertGroup: Create group of stock alerts.
StockAlertSubscription: user subscribe for a specific stock alert.
StockAlertGroupSubscription: user subscribe for a group of stock alerts.
ProductStockLog: If stock is updated, a log is created by using signal (product_stock_log)
stock_alert_trigger: this signal will be used to send specific trigger to specif user or group of users
    when a StockAlertTrigger is triggered.
```

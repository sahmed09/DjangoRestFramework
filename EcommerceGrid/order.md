## Order APIs
```
http://54.251.167.179:8000/api/order/
```

### User API:
http://54.251.167.179:8000/api/order/user_api/
```
Send GET request to view list of users:
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "username": "admin"
        },
        {
            "username": "Sakib"
        },
        {
            "username": "Jahid"
        }
    ]
}
```

### Customer API:
http://54.251.167.179:8000/api/order/customer_api/ <br>
Required fields: shop, first_name, last_name, email, mobile <br>
Example:
```
{
    "shop": {"slug": "rayans"},
    "first_name": "Admin",
    "last_name": "Admin",
    "email": "admin@gmail.com",
    "mobile": "1234560789"
}
```
Output:
```
{
    "id": 2,
    "first_name": "Admin",
    "last_name": "Admin",
    "email": "admin@gmail.com",
    "mobile": "1234560789",
    "shop": 2
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/order/customer_api/?email=admin@gmail.com&mobile=12345607891&shop__slug=rayans
Output:
[
    {
        "id": 1,
        "first_name": "Admin",
        "last_name": "Admin",
        "email": "admin@gmail.com",
        "user": 1
    }
]
```

### Area API:
http://54.251.167.179:8000/api/order/area_api/ <br>
Required fields: name <br>
Optional filed: parent_area <br>
Example:
```
{
    "slug": "airport",
    "parent_area": {"slug": "dhaka"}
}
```
Output:
```
{
    "id": 8,
    "name": "Airport"
    "slug": "airport",
    "parent_area": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/order/location_api/?slug=airport&parent_area__slug=dhaka
Output:
[
    {
        "id": 8,
        "name": "Airport",
        "slug": "airport",
        "parent_area": 1
    }
]
```

### DeliveryAgency API:
http://54.251.167.179:8000/api/order/delivery_agency_api/ <br>
Required fields: name, address, mobile, email <br>
Optional Fields: logo <br>
Example:
```
{
    "name": "Redex",
    "address": "Dhaka",
    "mobile": "12304567891",
    "email": "redex@gmail.com"
}
```
Output:
```
{
    "id": 1,
    "name": "Redex",
    "address": "Dhaka",
    "mobile": "12304567891",
    "email": "redex@gmail.com",
    "logo": null
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/order/delivery_agency_api/?name=Redex
Output:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Redex",
            "address": "Dhaka",
            "mobile": "12304567891",
            "email": "redex@gmail.com",
            "logo": null
        }
    ]
}
```

### ShopOrderStatus API:
http://54.251.167.179:8000/api/order/shop_order_status_api/ <br>
Required fields: shop, status <br>
Example:
```
{
    "shop": {"slug": "rayans"},
    "status": "Pending"
}
```
Output:
```
{
    "id": 4,
    "status": "Pending",
    "shop": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/order/shop_order_status_api/?status=&shop__slug=rayans
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "status": "Confirmed",
            "shop": 1
        },
        {
            "id": 2,
            "status": "Delivered",
            "shop": 1
        }
    ]
}
```

### OrderStatus API:
http://54.251.167.179:8000/api/order/order_status_api/ <br>
Required fields: shop_order_status, msg <br>
Example:
```
{
    "shop_order_status": {"status": "Delivered"},
    "msg": "Order Delivered"
}
```
Output:
```
{
    "id": 4,
    "shop_order_status": 2,
    "msg": "Order Delivered",
    "timestamp": "2021-10-29T19:42:33.865616"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/order/order_status_api/?shop_order_status__status=delivered&shop_order_status__shop__slug=rayans
Output:
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "shop_order_status": {
                "status": "Delivered"
            },
            "msg": "Order Delivered",
            "timestamp": "2021-10-29T19:42:33.865616"
        }
    ]
}
```

### Order API:
http://54.251.167.179:8000/api/order/order_api/ <br>
Required fields: customer, shop, mobile, email, address, area <br>
Optional field: order_status <br>
Example:
```
{
    "customer": {"mobile": "12345607891"},
    "shop": {"slug": "rayans"},
    "mobile": "12345607891",
    "email": "admin@gmail.com",
    "address": "Dhaka",
    "area": {"slug": "dhanmondi"},
    "order_status": {"shop_order_status": {"status": "Pending"}}
}
```
Output:
```
{
    "id": 10,
    "customer": 1,
    "shop": 1,
    "transaction_id": "0x1187bffea898e0876",
    "mobile": "12345607891",
    "email": "admin@gmail.com",
    "address": "Dhaka",
    "date_ordered": "2021-10-29T19:55:50.449782",
    "order_status": 5,
    "area": 2
}
```
Filtering Example:
```
http://127.0.0.1:8000/api/order/order_api/?mobile=12345607891&transaction_id=0x1187bffea898e0876&order_status__shop_order_status__status=confirmed
Output:
[
    {
        "id": 10,
        "customer": {
            "id": 1,
            "shop": {
                "name": "Rayans",
                "slug": "rayans"
            },
            "mobile": "12345607891"
        },
        "shop": {
            "name": "Rayans",
            "slug": "rayans"
        },
        "transaction_id": "0x1187bffea898e0876",
        "mobile": "12345607891",
        "email": "admin@gmail.com",
        "address": "Dhaka",
        "date_ordered": "2021-10-29T19:55:50.449782",
        "order_status": 6,
        "area": 2
    }
]
```
Filter by Area
```
http://54.251.167.179:8000/api/order/order_api/?area=mohammadpur
or
http://54.251.167.179:8000/api/order/order_api/?area=dhaka
Or Filter by area(Parent area or child area):
If search by child area, then all the order of that area will be shown.
If search by parent area, then all the order of that area will be shown where child area can be different.

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 10,
            "customer": {
                "id": 1,
                "shop": {
                    "name": "Rayans",
                    "slug": "rayans"
                },
                "mobile": "12345607891"
            },
            "shop": {
                "name": "Rayans",
                "slug": "rayans"
            },
            "transaction_id": "0x1187bffea898e0876",
            "mobile": "12345607891",
            "email": "admin@gmail.com",
            "address": "Dhaka",
            "date_ordered": "2021-10-29T19:55:50.449782",
            "order_status": 6,
            "area": 2
        },
        {
            "id": 11,
            "customer": {
                "id": 1,
                "shop": {
                    "name": "Rayans",
                    "slug": "rayans"
                },
                "mobile": "12345607891"
            },
            "shop": {
                "name": "Rayans",
                "slug": "rayans"
            },
            "transaction_id": "0x1187bffeb94f4ea8a",
            "mobile": "1234560789",
            "email": "admin@gmail.com",
            "address": "Dhaka",
            "date_ordered": "2021-10-29T20:00:22",
            "order_status": 5,
            "area": 3
        }
    ]
}
```

### OrderItem API:
http://54.251.167.179:8000/api/order/order_item_api/ <br>
Required fields: product, order, quantity <br>
Example:
```
{
    "product": {"product": {"slug": "walton-double-door-non-frost-fridge"}},
    "quantity": 1,
    "order": {"transaction_id": "0x1187bf89c6a76d9ed"}
}
```
Output:
```
{
    "id": 4,
    "product_name": "Acer Super Speedy Gaming Mouse",
    "quantity": 1,
    "price": "5000.00",
    "product": 1,
    "order": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/order/order_item_api/?order__transaction_id=0x1187bf89c6a76d9ed
Output:
[
    {
        "id": 3,
        "product_name": "Singer Double Door Frost Fridge",
        "quantity": 1,
        "price": "80000.00",
        "product": 3,
        "order": 1
    } ............
]
```

### DeliveryAgencyOrders API:
http://54.251.167.179:8000/api/order/delivery_agency_orders_api/ <br>
Required fields: agency, order <br>
Example: <br>
```
Add Delivery agency for a group or orders. Send agency name in url
Send POST reqquest:

http://54.251.167.179:8000/api/order/delivery_agency_orders_api/?agency=redex
{
    "data": [
        {
            "transaction_id": "0x1187bffeb94f4ea8a"
        },
        {
            "transaction_id": "0x1187bffea898e0876"
        }
    ]
}
```
Output:
```
{
    "message": "Delivery Agency Assigned Successfully"
}

If agency exists for these orders:
{
    "message": "Delivery Agency For this order already exists"
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/order/delivery_agency_orders_api/?agency__name=redex&order__transaction_id=0x1187bffeb94f4ea8a
Output:
[
    {
        "id": 21,
        "ordered_date": "2021-10-29T20:09:44.925343",
        "agency": 1,
        "order": 11
    }
]
```

```
Models:
Customer: Create shop based customer.
Area: Create Delivery area. Used self referencing for creating parent child relation. if parent_area=None,
    it itself a parent area, otherwise a child area.
DeliveryAgency: Creates Delivery Agency.
ShopOrderStatus: Creates shop based order sattus.
OrderStatus: Order status with a message for a shop order status.
Order: Creates order for a customer in a specific shop.
OrderItem: Add order items in an order. 
    If an item is orderd, it triggers a signal (update_stock) which updates the stock.
DeliveryAgencyOrders: Assign delivery agency for an order.
```

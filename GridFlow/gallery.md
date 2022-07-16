## Gallery APIs
```
http://54.251.167.179:8000/api/gallery/
```

### Album API:
http://54.251.167.179:8000/api/gallery/album_api/ <br>
Required fields: name <br>
Example:
```
{
    "name": "album_name"
}
```
Output:
```
{
    "id": 1,
    "name": "album_name"
}
```

### AlbumItems API:
http://54.251.167.179:8000/api/gallery/album_items_api/ <br>
Required fields: album, image, ordering_priority <br>
Example:
```
file field will be used here
```
Output:
```
{
    "id": 1,
    "image": "https://gridflow.s3.amazonaws.com/eset-with-free-tshirt-500x500.jpg?AWSAccessKeyId=AKIATGA5PGPHCOSBJBGE&Signature=Ijxo8umiJWkf0AjwxFaWb%2FWGj08%3D&Expires=1633008340",
    "ordering_priority": 1,
    "album": 1
}
```
Filtering Example:
```
http://54.251.167.179:8000/api/gallery/album_items_api/?album__name=
```

```
Models:
Album: Creates an album for shop, branch, product etc. anything.
AlbumItems: Add images to the album with a ordering priority level (0-10)
```

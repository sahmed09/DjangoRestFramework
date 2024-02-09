### Generating Access and Refresh Token:
http://54.251.167.179:8000/api/token/
```
Send a POST request
{
    "username": "username",
    "password": "password"
}
```
Output:
```
{
    "refresh": "refresh_token",
    "access": "access_token"
}
```

### Generating New Access Token:
http://54.251.167.179:8000/api/token/refresh/
```
Send a POST request
{
    "refresh": "enter_previous_refresh_token"
}
```
Output:
```
{
    "access": "new_access_token"
}
```

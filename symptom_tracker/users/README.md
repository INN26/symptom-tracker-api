# Symptom Tracker API

## To test the API routes, use an application like POSTMAN or cURL

### Users App Routes

To register a user, use a POST request to the route:

``` bash
http://localhost:8000/api/register/
```

This route accepts form data with the format:

> *email*, *name*, *password*, *role*

After successful registration the route will return:

``` python
{
"id":1,
"email":"Entered Email",
"name":"Entered Name",
"role":"Entered Role"
}
```

To login we need use a POST request to the route:

``` bash
http://localhost:8000/api/login/
```

This route accepts form data with the format:

> *email* and *password*

After successfully logging in, the route will return:

``` python
{
    "message": "Login successful",
    "user": {
        "id": 4,
        "email": "user@email.com",
        "name": "John Doe",
        "role": "patient"
    }
}
```

Happy Surfing!

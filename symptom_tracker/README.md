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

### Symptoms App Routes

To enter a new symptom a user needs to be logged in. This user then sends a POST request to the route:

``` bash
http://localhost:8000/api/symptoms/
```

This route takes in form data with the format:

> **symptom_type** and **severity** *(symptom severity, e.g mild)*

After successfully writing the symptom in the database, the route will return:

``` python
{
    "id": 3,
    "user": 2,
    "date_logged": "2025-04-02T12:07:36.927111Z",
    "symptom_type": "Headache",
    "severity": "Mild"
}
```

To read a user's stored symptoms, the user reading the data needs to be logged in and authorized to read the data. This user then sends a GET request to the route:

``` bash
http://localhost:8000/api/symptoms/
```

This request does not require any form data.

After successfully getting the symptoms from the database, this route will return all the symptoms linked a user in a list, as follows:

``` python
[
    {
        "id": 1,
        "user": 2,
        "date_logged": "2025-04-01T12:38:01.472617Z",
        "symptom_type": "Headache",
        "severity": "8"
    },
    {
        "id": 2,
        "user": 2,
        "date_logged": "2025-04-01T12:49:26.816295Z",
        "symptom_type": "Headache",
        "severity": "4"
    },
    {
        "id": 3,
        "user": 2,
        "date_logged": "2025-04-02T12:07:36.927111Z",
        "symptom_type": "Headache",
        "severity": "Mild"
    }
]
```

To read the daily trend in which a user logs their symptoms, the user reading the trend needs to be logged in and authorized to read the data. Then this user sends a GET request to the route:

``` bash
http://localhost:8000/api/symptoms/trends/
```

After successfully fetching the trend in which symptoms occur from the database, the route will return a daily count of the logged symptoms linked to a user, in a list, as follows:

``` python
[
    {
        "date": "2025-03-29",
        "count": 1
    },
    {
        "date": "2025-03-31",
        "count": 3
    },
    {
        "date": "2025-04-01",
        "count": 2
    },
    {
        "date": "2025-04-02",
        "count": 1
    }
]
```

To read the daily trend in which a user logs one particular symptom, the user reading the trend needs to be logged in and authorized to read the data. Then this user sends a GET request with the symptom parameter to the route:

``` bash
http://localhost:8000/api/symptoms/trends/?symptom=headache
```

After successfully fetching the trend in which one defined symptom occurs in, from the database, the route will return a daily count of that symptom, for the authorized user linked to that symptom, in a list, as follows:

``` python
[
    {
        "date": "2025-03-31",
        "count": 2
    },
    {
        "date": "2025-04-02",
        "count": 1
    }
]
```

### Notications App Routes

To add a notification or reminder for a user, make a POST request to the route:

``` bash
http://localhost:8000/api/notifications/
```

This route accepts form data with the format:

> *message*

After successfully logging a reminder the route will return:

``` python
{
    "id": 2,
    "user": 5,
    "message": "It is time to log your symptoms!",
    "sent_at": "2025-04-04T08:49:00.738757Z"
}
```

To view a user's logged notifications, make a *GET* request to the route:

``` bash
http://localhost:8000/api/notifications/list/
```

This route will return all the system reminders linked to a user in a list, as follows:

``` bash
[
    {
        "id": 1,
        "user": 5,
        "message": "\"It is time to log your symptoms\"",
        "sent_at": "2025-04-04T08:43:56.281474Z"
    },
    {
        "id": 2,
        "user": 5,
        "message": "It is time to log your symptoms!",
        "sent_at": "2025-04-04T08:49:00.738757Z"
    }
]
```

Happy Surfing!

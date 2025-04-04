# Symptom Tracker API

## To test the API routes, use an application like POSTMAN or cURL

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

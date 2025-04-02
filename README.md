# Symptom Tracker API

To run this start by cloning the repo

```
git clone https://github.com/INN26/symptom-tracker-api.git
```

Create a virtual environment using

For Linux
```
python3 -m venv venv
```

or For Windows

```
python -m venv venv
```

# Install requirements using 
To install the requirements use
```
pip install -r requirements.txt
```

Navigate to the symptom_tracker folder using
```
cd symptom_tracker
``` 

# Run Migrations
To make migrations use:
```
python manage.py makemigrations
``` 
and to write the changes to the database use:

```
python manage.py migrate
```


# Run the server using 
```
python manage.py runserver
```



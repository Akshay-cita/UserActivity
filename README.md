# UserActivity
## Problem Statement:
Design and impliment a Django application with User and Activity models,write a custom management command to populate the database with some dummy data,and design an API to serve that data in the JSON format.
## Django Model:
User and ActivityPeriod
## Buit With:
* [Django](https://www.djangoproject.com/)
* [DJANGO-REST API Framework](https://www.django-rest-framework.org/api-guide/fields/)-Serializer
* [Django-seed package](https://github.com/Brobin/django-seed)- To populate the database with dummy data

## Package Installation Guide
* Django-seed `pip install django-seed`

Add it to your installed apps in ``settings.py``::

    INSTALLED_APPS = (
        ...
        'django_seed',
    )

* pytz `pip install pytz`

## Populating the database with dummy data
In the project directory, you can run:
### `python populate_data.py`
Here I'm used Django-seed package.Initial step is to run `populate_data.py` and then run `python manage.py runserver`
## Things I have done
* Created a API `userlist`that served a JSON file describes a list of users and their corresponding periods of activity across multiple month
* A python script with `django-seed` package to populate database with dummy data(`populate_data.py`)
### Project Link:





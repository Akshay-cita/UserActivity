# UserActivity
## Problem Statement:
Design and impliment a Django application with User and Activity models,write a custom management command to populate the database with some dummy data,and design an API to serve that data in the JSON format.
## Django Model:
User and ActivityPeriod
## Buit With:
* [Django](https://www.djangoproject.com/)
* [DJANGO-REST API](https://www.django-rest-framework.org/api-guide/fields/)-Serializer
* [Django-seed package](https://github.com/Brobin/django-seed)- To populate the database with dummy data

## Package Installation Guide
* Django-seed `pip install django-seed`
* pytz `pip install pytz`

## Populating the database with dummy data
In the project directory, you can run:
### `python populate_data.py`
Here I'm used Django-seed package.Initial step is to run `populate_data.py` and then run `python manage.py runserver`




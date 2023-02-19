Django REST API
This is a Django REST API that allows users to log in with their email and password, and retrieve a list of all users.

Installation
To install the required packages for this project, run the following command:

    pip install -r requirements.txt

Configuration
To configure the API, you will need to update the settings in settings.py. You should update the following settings:

SECRET_KEY: Set this to a unique, random string.
DEBUG: Set this to False in production.
ALLOWED_HOSTS: Set this to a list of allowed hostnames for your application.
Running the API
To run the API, you can use the built-in Django development server. Run the following command:


    python manage.py runserver

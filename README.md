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
 
This will start the server on http://localhost:8000/.

Endpoints

Authentication
POST /auth/users/login/
This endpoint allows users to log in with their email and password. The request should be in the following format:
    
    {
        "email": "user@example.com",
        "password": "secret"
    }
  

If the login is successful, the API will return a token that can be used for authentication. The response will be in the following format:

    {
        "token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
    

Users

GET /auth/users/
This endpoint returns a list of all users. To access this endpoint, you will need to include the authentication token in the request headers. The token should be in the following format:

    Authorization: Token xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

The API will return the list of users in the following format:


        {
        "users":     [
         {
                "email": "user1@example.com",
                "username": "user1"
            },
            {
                "email": "user2@example.com",
                "username": "user2"
            }
        ]
    }


License
This project is licensed under the MIT License. See the LICENSE file for details.

















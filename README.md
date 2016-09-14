# Secret Santa Reboot

A webapp to simplify your secret santa planning.

## Features

### Working
- User signup & login/logout
- Create a group
- Create an exchange
- View an exchange

### To do
This project is a work in progress. Below is a list of features still to be implemented.

- Group manager can modify an exchange
- User can create/modify their gift list for a particular exchange
- Limit viewing & choices by logged-in user permissions
- Login by email instead of by username
- User can edit their profile (set their name, etc.)
- Better display of current/recent exchanges, how to handle groups

## How to run

### Development

#### Clone the project
```git clone ...```

#### Install pip and virtualenv if you haven't already.

#### Create a virtual environment and install the dependencies
- ```virtualenv .pyvirtual```
- ```source .pyvirtual/bin/activate```
- ```pip install -r requirements.txt```

#### Initialize the database
- ```cd secretsanta```
- ```python manage.py makemirations```
- ```python manage.py migrate```

#### Create the admin user
- ```python manage.py createsuperuser```

#### Run the development server
- ```python manage.py runserver```


### Production

#### Secret keys
Make sure you generate & protect your secret keys...

#### Production server
You can use any WSGI-compatible production server to run the project.
The easiest way to run it is using ```gunicorn```.

- ```gunicorn```

## Acknowlegements

- Built with Django
- Flatly Bootstrap style from Bootswatch

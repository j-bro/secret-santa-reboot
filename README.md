# Secret Santa Reboot

A webapp to simplify your secret santa planning.

(REBOOT) because it's reviving my [pige-de-noel](https://github.com/j-bro/pige-de-noel) project.

## Features

### Working
- User signup, login, logout
- Create, view, modify, delete a group
- Create, view, modify, delete an exchange
- Group manager can activate an exchange, which assigns a drawn member to each group member

### To do
This project is a work in progress. Below is a list of features still to be implemented.

- User can create/modify their gift list for a particular exchange
- Limit viewing & choices by logged-in user permissions
- Login by email instead of by username
- User can edit their profile (set their name, etc.)
- Better display of current/recent exchanges, how to handle groups

## How to run

### Development

#### Clone the project

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
The easiest way to run it is using [gunicorn](http://gunicorn.org).

- ```cd secretsanta```
- ```gunicorn secretsanta.wsgi```

## Acknowlegements

- Built with Django
- Flatly Bootstrap style from Bootswatch

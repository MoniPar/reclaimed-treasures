# Overview

Vera's Reclaimed Treasures is an educational fullstack website based on business logic used to control a centrally owned dataset.  It has an authentication mechanism and provides paid access based on the dataset in the purchasing of products.

_____

# Deployment

This project was developed in [CodeAnywhere](https://app.codeanywhere.com/) Cloud IDE using [Code Institute's Full Template](https://github.com/Code-Institute-Org/ci-full-template).  The following describes the process undertaken to set up the Django project using a postgreSQL database instance on [ElephantSQL](https://www.elephantsql.com/), an [Amazon AWS S3 Bucket](https://aws.amazon.com/) for media and static file storage and deployment to [Heroku](https://www.heroku.com/).  

## Setup

1. Create a new GitHub repository using the [Code Institute's Full Template](https://github.com/Code-Institute-Org/ci-full-template) which preinstalls all the tools needed to get started.  If you do not have access to this you need to pre-install Python and all requirements into your IDE.
2. Once your repository has been created on GitHub, copy the repository URL and log into [CodeAnywhere](https://app.codeanywhere.com/) with your GitHub account.
3. Click on the 'New Workspace' button on your dashboard and paste in the copied repository URL.  Click 'Create'. This will create your new workspace which can be accessed from the [CodeAnywhere Dashboard](https://app.codeanywhere.com/).
4. In your new workspace navigate to the 'Terminal' tab in the top menu and click on 'New Terminal'. This will open a terminal at the bottom of the workspace where you can run the following commands to install Django and supporting libraries.
   * `pip3 install 'django<4' gunicorn`  - This installs [Django 3.2](https://www.djangoproject.com/start/overview/) and the server [gunicorn](https://gunicorn.org/) used to run the project on Heroku.
   * `pip3 install dj_database_url==0.5.0 psycopg2`  - This installs the [postgreSQL](https://www.postgresql.org/) relational database management system along with [psycopg2](https://www.psycopg.org/docs/) and adapter for Python.
   * `pip3 freeze --local > requirements.txt`  - This creates the requirements.txt file and adds Django and the installed supporting libraries to it.
5. Create a new Django project and give it the name of the website. `django-admin startproject project_directory .`  - Don't forget the (.) dot to create the project in the current directory.
6. Create the first app. I started with the home app. `python3 manage.py startapp home`
7. Add the new app to the INSTALLED_APPS in settings.py.

   ```python
   INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        #  Custom apps
        'home',
    ]
    ```

8. Create a basic .gitignore file `touch .gitignore` (you might already have this if you're using CI's Full Template). Then add:
   * `*.sqlite3`  - so as not to commit the development database to version control.
   * `.pyc` and `__pycache__`  - to ignore compiled Python code not needed in version control.
9. Run the project to make sure that everything is working properly using the `python3 manage.py runserver` command and exposing port 8000. If working on CodeAnywhere, you may get a 'DisallowedHost at /' error.  Copy the URL of your running CodeAnywhere project to the ALLOWED_HOSTS variable in settings.py and run it again. `ALLOWED_HOSTS = ['8000-githubusername-gitrepositoryname-abcde12fgh.us2.codeanyapp.com']` - Do not add the 'https://' at the start or the trailing '/' at the end. You should now get the 'Install worked successfully' page below.
![Django Successful Installation page](docs/django_successful.png)
10. Stop the server ('ctrl + c' on windows, 'cmd + .' on mac) and run the initial migrations using the `python3 manage.py migrate` in the terminal.
11. Create a superuser so that you can log in to the Admin panel. `python3 manage.py createsuperuser` and enter your username, email and password. The skeleton of the project is now complete.

## First Deployment

With the skeleton of the project running locally, it is best to prepare it for deployment on Heroku at this early stage.

### Create the Heroku App

1. Login to [Heroku](https://www.heroku.com/) and click on the top right button ‘New’ on the dashboard.
2. Click 'Create new app'.
3. Give your app a unique name and select the region closest to you.
4. Click on the 'Create app' button.

### Create the postgreSQL Database

Since the database provided by Django is only accessible within Gitpod, a new database suitable for production needs to be created in order for Heroku to be able to access it.  The following steps create a new postgreSQL database instance, hosted on [ElephantSQL](https://www.elephantsql.com/).

1. Login to ElephantSQL and click on the top right button 'Create New Instance'.
2. Give your plan the name of the project and select the Tiny Turtle (Free) plan.  The 'Tags' field can be left empty.
3. Click on 'Select Region'. Select a data centre near you.  Choose another region if there is none in your region yet. Click 'Review'.
4. Make sure your plan is correct and click 'Create Instance'.
5. Return to the dashboard and click on this project's instance you just created. This will open up the 'Details' page where the link to the URL is displayed.  This needs to be added to the env.py file in the project's directories as well as to the Heroku Config Vars so copy it and keep this tab open.

### Create an env.py file

With the database created, it now needs to be connected with the project.  Certain variables need to be kept private and should not be published to GitHub.  In order to keep these variables hidden, it is important to create an env.py file and add it to .gitignore.  

1. Run the `touch env.py` command in the terminal to create the env.py file.
2. Import os and set the DATABASE_URL variable using the `os.environ` method and add the URL copied from instance created above to it here, like so: `os.environ[“DATABASE_URL”] = ”postgres://ElephantSQLcopiedURL”`
3. The Django application requires a SECRET_KEY to encrypt session cookies.  Set this variable to any string you like or generate a secret key on this [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/).
   `os.environ[“SECRET_KEY”] = ”longSecretString”`

### Modify settings.py

It is important to make the Django project aware of the env.py file and to connect the workspace to the new database.

1. Open up the settings.py file and add the following code. The if statement acts as a safety net for the application in case it is run without the env.py file.

    ```python
    import os  
    import dj_database_url  

    if os.path.isfile('env.py'):
        import env
    ```

2. Remove the insecure secret key provided by Django further down and reference the variable in the env.py file, like so:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ```

3. Hook up the database using the dj_database_url import added above.  Comment out the original DATABASES variable provided by Django which connects the Django application to the created db.sqlite3 database within your repo.  This database is not suitable for production so add the following code instead:

    ```python
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    } 
    ```

    Note: If you prefer to work with the db.sqlite3 one in development then use the following code to use it if the external database is not yet hooked up.

    ```python
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```

4. Save and migrate this database structure to the newly connected postgreSQL database.  Run the migrate command `python3 manage.py migrate` in your terminal.

5. To make sure the application is now connected to the remote database hosted on ElephantSQL, head over to your ElephantSQL dashboard and select the newly created database instance. Select the 'Browser' tab on the left and click on 'Table queries'.  This displays a dropdown field with the database structure which has been populated from the Django migrations. If you select 'auth_user' and click on the 'Execute' button on the right, you should be able to see your superuser details displayed.  This confirms your tables have been created and you can add data to your database.

6. If you don't see your superuser details displayed run the `python3 manage.py createsuperuser` command again, give yourself a Username, email and password and go over step 5 above again.

### Connect the database to Heroku

1. Open up the Heroku dashboard, select the project's app and click on the 'Settings' tab.
2. Click on 'Reveal Config Vars' and add the DATABASE_URL with the value of the copied URL (without quotation marks) from the database instance created on ElephantSQL.
3. Also add the SECRET_KEY with the value of the secret key added to the env.py file.
4. If using GitPod another key needs to be added in order for the deployment to succeed.  This is PORT with the value of 8000.
5. To help get the project deployed without static files you need to add one more temporary variable.  This needs to be removed before deploying the full project.  Use DISABLE_COLLECTSTATIC as the key and '1' as the value.

### Setup the Templates directory

In settings.py scroll down to the TEMPLATES variable to instruct Django to store the root templates directory in the DIRS setting, like so:

```python
'DIRS' = [
    os.path.join(BASE_DIR, 'templates'),
]
```

This is where the custom allauth directory will also be set.

### Add Heroku Host Name

In settings.py scroll to ALLOWED_HOSTS and add the Heroku host name before the URL of your running CodeAnywhere project. This should be the Heroku app name created earlier followed by .herokuapp.com.
`ALLOWED_HOSTS = ['heroku-app-name.herokuapp.com', '8000-githubusername-gitrepositoryname-abcde12fgh.us2.codeanyapp.com']`

### Create the Process file

1. Create the media, static and templates directories at the root level next to the manage.py file.
2. At the root level again, create a new file called 'Procfile' with a capital 'P'. This tells Heroku how to run this project. In this file add the following code, including the name of your project directory. `web: gunicorn project_directory.wsgi:application`
    * 'web' tells Heroku that this a process that should accept HTTP traffic.
    * 'gunicorn' is the server used
    * 'wsgi' stands for web services gateway interface and is a standard that allows Python services to integrate with web servers

_____

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **March 3rd, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

_____

Happy coding!

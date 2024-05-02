# Introduction

This project for finloge

### Clone the repository:

    git clone `https://github.com/abhi-9791/finloge_project`

### Create a virtual environment and activate it
    python -m venv `fin_env`
    venv\Scripts\activate

### Install Django

After activating the venv, install Django using the following command:
    pip install django

# Creation of Project and App

After installation, create the project and app using the following commands:
    django-admin startproject finloge_project
    py manage.py startapp finloge_app

### Requirements for the Project

Install project dependencies:

     pip install -r requirements/local.txt

Create a superuser (optional):
    python manage.py createsuperuser

### Running the Server

To run the development server, use the following command:
    python manage.py runserver

The server will start at http://localhost:8000/

### Project Information

For more information about our project, visit:
    http://localhost:8000/coming_soon

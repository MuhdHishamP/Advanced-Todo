# AlgoBulls Backend Developer (Web) Coding Assignment - Django To-Do List App

## Overview

This repository contains the backend code for a simple To-Do List application implemented using Django. I have deployed the Postgres database on Railway and the Django app on Vercel to complete this project.


## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.

## Usage

Run the Django development server:

```bash
python manage.py runserver
```
## Access the app
Access the app at - [Todo DRF](https://todo-app-jade-sigma.vercel.app/api/todos/) and [Tags DRF of Todo list items](https://todo-app-jade-sigma.vercel.app/api/tags/) (Credentials are given below).

- **Username:** hisham 
- **Password:** hnfhnfhnf


## Django Admin
- **URL:** [Django Admin URL](https://todo-app-jade-sigma.vercel.app/admin) (Credentials are given below).
- **Username:** hisham 
- **Password:** hnfhnfhnf

## API Endpoints
- **CREATE a Todo item:** POST at `/todo/`
- **READ one Todo item:** GET at `/todo/{id}/`
- **READ all Todo items:** GET at `/todo/`
- **UPDATE a Todo item:** PUT at `/todo/{id}/`
- **DELETE a Todo item:** DELETE at `/todo/{id}/`
- **CREATE a Todo item:** POST at `/tags/`
- **DELETE a Todo item:** DELETE at `/tags/{id}/`

  
Use Basic Authentication for API requests.

## Coverage Summary

![Coverage Summary](https://github.com/MuhdHishamP/Algo-Todo-3/assets/99111049/bd4b980f-8584-4c75-aba6-df9eb171cb2c)




## Testing
Run tests:

```bash
python manage.py test
```

# Continuous Integration

GitHub Actions automatically run tests and linting on every commit push.






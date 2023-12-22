# Django To-Do List App

## Overview

This repository contains the backend code for a simple To-Do List application implemented using Django.


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
- **CREATE:** POST at `/api/todo/`
- **READ one:** GET at `/api/todo/{id}/`
- **READ all:** GET at `/api/todo/`
- **UPDATE:** PUT at `/api/todo/{id}/`
- **DELETE:** DELETE at `/api/todo/{id}/`
  
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






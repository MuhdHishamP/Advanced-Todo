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
Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Django Admin
- **URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Credentials:** admin/admin

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






# Django To-Do List App

## Overview

This repository contains the backend code for a simple To-Do List application implemented using Django.

## Prerequisites

- Python 3.11+
- Django 4.2.7+
- Django Rest Framework 3.14.0+

## Installation

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.

## Usage

Run the Django development server:

```bash
python manage.py runserver
```
# Access the app
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

## Testing
Run tests:

```bash
python manage.py test



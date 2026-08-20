# Django Blog CRUD

A focused Django coursework project demonstrating create, read, update, and delete operations for blog posts with server-rendered forms and templates.

## Features

- Create and list blog posts
- Read an individual post
- Edit existing content through a `ModelForm`
- Confirm and delete a post
- Manage posts through Django admin
- Store local development data in SQLite

## Run locally

```bash
cd crudproject
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py test core
python manage.py runserver
```

Open `http://127.0.0.1:8000`. To use the admin interface, create local credentials with `python manage.py createsuperuser`.

## Scope

This is an educational CRUD application. SQLite, `DEBUG=True`, and the fallback development key are for local use only. Set `DJANGO_SECRET_KEY` and production-safe settings before any deployment.

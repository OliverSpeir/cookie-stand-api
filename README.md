# LAB - 34

## Project: DRF API / Frontend Template

### Author: Oliver Speir

### Description

- Cookie stand API
    - built from template
    - hosting on elephantSQL

### Setup

Run:
- clone and cd into directory
- `docker compose up`
- or run outside of container by:
  - clone and create venv then activate venv `pip install -r requirements.txt`
  - then run `gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 4` or `python manage.py runserver` for development server

Test:
- While server is running  is running:
- `curl -d '{"username":"dev", "password":"uncommon"}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:8000/api/token/`
### Resources

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [postgresql](https://www.postgresql.org/)
- [Green Unicorn (gunicorn)](https://gunicorn.org/)
- [WhiteNoise](https://whitenoise.evans.io/en/latest/)

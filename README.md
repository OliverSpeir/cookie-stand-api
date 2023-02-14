# LAB - 34

## Project: Cookie Stand API

- [api vercel](https://cookie-stand-api-eta.vercel.app/) (connected to elephantSQL)
- [front end vercel](https://cookie-stand-admin-livid.vercel.app/)
- [front end repo](https://github.com/OliverSpeir/cookie-stand-admin)

### Author: Oliver Speir

### Description

- Cookie stand API
    - built from template
    - can be connected to postgresql docker container, elephantSQL, or sqlite db built into django

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
- [elephantSQL](https://www.elephantsql.com/)

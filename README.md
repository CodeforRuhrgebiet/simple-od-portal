# simple-od-portal

A really simple Open Data portal for cities that don't have one.

## development setup

(if you like to use docker, see below).

This project was initially developed under Python 3, but *should* work under 2, too (plz test).

Use your preferred python packaging management / virtualization system. Recommendation: [virtualenv](https://virtualenv.pypa.io/en/stable/)

Then, follow these steps to get the app running (inside your python environment):

`pip install -r requirements.txt.`

`./manage.py migrate`

`./manage.py runserver`

Open your browser at http://127.0.0.1:8000

## add datasets

The `datasets.models.Dataset`-model is readonly in the admin, because the **source of truth** should be a [repo like this](https://github.com/CodeforRuhrgebiet/offenes-datenportal) and this app only pulls this repo and loads the datasets into the databse. See the repos `README.md` for details how to add datasets there.

Clone the dataset to somewhere in your project and adjust the `DATASETS_*`-settings in `simple_od_portal/settings.py`.

Then, the app can find the datasets and import them via:

`./manage.py import_from_github`

## theme development

### templates

All templates should go into the `theme`-app. See `./theme/templates/*` for examples.

### style

There is really simple `sass`-based css in `./theme/src/`

Use the sass-compiler you prefer on your system. Only requirement: css output must be in `./theme/static/css/main.css`


## development setup with docker

1. run migrations `docker-compose run web python manage.py migrate`

2. setup admin user `docker-compose run web python manage.py createsuperuser`

3. start server `docker-compose up`

open browser [http://localhost:8000](http://localhost:8000)

login at [http://localhost:8000/admin/](http://localhost:8000/admin/)

## deployment

**DON'T USE DJANGOS BUILT-IN RUNSERVER!!** - it is only meant to use for local development. Instead, have a look at the [official docs for deployment](https://docs.djangoproject.com/en/1.10/howto/deployment/).

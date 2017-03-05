# simple-od-portal
A really simple Open Data portal for cities that don't have one.

# usage with docker

1. run migrations `docker-compose run web python manage.py migrate`

2. setup admin user `docker-compose run web python manage.py createsuperuser`

3. start server `docker-compose up`

open browser [http://localhost:8000](http://localhost:8000)

login at [http://localhost:8000/admin/](http://localhost:8000/admin/)

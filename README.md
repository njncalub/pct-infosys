pct-infosys
===========

A simple information system project using Django.

-----------

Install dependencies:
> python 2.7
> virtualenv
> pip

Create and activate virtualenv:
> virtualenv env
> source env/bin/activate

Install requirements using pip:
> pip install -r requirements/requirements.txt

Create and migrate database:
> ./manage.py syncdb
> ./manage.py migrate

Create a superuser account:
> ./manage.py createsuperuser

Collect static files to server's static folder:
> ./manage.py collectstatic

Run server:
> ./manage.py runserver
> Login at http://127.0.0.1:8000/admin

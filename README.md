pct-infosys
===========

A simple information system project using Django.

-----------

Create and activate virtualenv:
> virtualenv env
> source env/bin/activate

Install requirements using pip:
> pip install -r requirements/requirements.txt

Create database:
> ./manage.py syncdb

Collect static files to server's static folder:
> ./manage.py collectstatic

Run Server:
> ./manage.py runserver

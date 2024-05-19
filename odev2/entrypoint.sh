#!/bin/bash

python manage.py makemigrations
python ./manage.py migrate

python manage.py loaddata ./items.json
python ./manage.py runserver 0.0.0.0:3000
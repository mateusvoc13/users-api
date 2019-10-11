#!/bin/bash

# Collect static files
echo "Collect static files"

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

python manage.py initadmin

python manage.py populate_db

echo "Running Server"
python3 manage.py runserver 0.0.0.0:8990

#!/usr/bin/env bash

python3 -m pip install --upgrade pip
python3 -m venv venv
pip install django psycopg2 

source ./venv/bin/activate

python3 manage.py migrate 
python3 manage.py runserver 

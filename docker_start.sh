#!/bin/sh

backend_port=$1

sleep 2

python ./app/manage.py migrate

python ./app/manage.py runserver 0.0.0.0:$backend_port

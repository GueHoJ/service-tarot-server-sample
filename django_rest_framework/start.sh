#!/bin/bash

# Define the log file path
LOGFILE="/django_rest_framework/startup.log"

# Define the access log file path
ACCESS_LOG="/django_rest_framework/web_socket_access.log"

# Create or clear the log file at the start
echo "Starting Django setup process..." > $LOGFILE

# Activate virtual environment
source /venv/bin/activate

# Run collectstatic
echo "Collecting static files..." >> $LOGFILE
python manage.py collectstatic --noinput

# Run makemigrations
echo "Making migrations..." >> $LOGFILE
python manage.py makemigrations

# Run migrate
echo "Applying migrations..." >> $LOGFILE
python manage.py migrate --database default

# Create superuser
echo "Creating superuser..." >> $LOGFILE
python manage.py makesuperuser

# Start Gunicorn
echo "Starting Gunicorn..." >> $LOGFILE
#gunicorn project.wsgi:application --bind 0.0.0.0:8000 --timeout 600 --workers 12 --threads 8 --preload
daphne -b 0.0.0.0 -p 8000 \
        --access-log $ACCESS_LOG \
        --ping-interval 30 \
        project.asgi:application

# Start Celery worker (optional)
#echo "Starting Celery worker..." >> $LOGFILE
#celery -A project worker --loglevel=info >> $LOGFILE 2>&1 &

# Start Celery beat (optional)
#echo "Starting Celery beat..." >> $LOGFILE
#celery -A project beat --loglevel=info >> $LOGFILE 2>&1 &

# Start Celery flower (optional)
#echo "Starting Celery flower..." >> $LOGFILE
#celery -A project flower --loglevel=info >> $LOGFILE 2>&1 &

# Log that the script has finished running
echo "Startup process complete." >> $LOGFILE

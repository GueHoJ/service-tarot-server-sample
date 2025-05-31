#!/bin/bash

# Define the log file path
LOGFILE="startup.log"

# Create or clear the log file at the start
echo "Starting Django setup process..." > $LOGFILE

# Activate virtual environment
source venv/bin/activate

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
gunicorn --worker-class sync project.wsgi:application --bind 0.0.0.0:8081 --timeout 600 --workers 1 --threads 2

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

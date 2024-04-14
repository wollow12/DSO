#!/bin/sh

# Navigate to the directory where your Flask app is located
cd /app

# Start Gunicorn with your Flask app
gunicorn --workers 4 --bind 127.0.0.1:9090 'wsgi:app' &

# Proceed to start Nginx
nginx -g 'daemon off;'

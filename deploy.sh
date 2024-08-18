#!/bin/bash

# Update and install dependencies
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev nginx curl -y

# Install virtualenv
pip3 install virtualenv

# Set up the virtual environment
virtualenv venv
source venv/bin/activate

# Install Django and Gunicorn
pip install django gunicorn psycopg2-binary

# Set up the Django application
cd /path/to/pricing_app
python manage.py migrate
python manage.py collectstatic

# Configure Gunicorn
gunicorn --workers 3 --bind unix:/path/to/pricing_app.sock pricing_app.wsgi:application

# Set up Nginx
sudo rm /etc/nginx/sites-enabled/default
sudo nano /etc/nginx/sites-available/pricing_app

# Add the following content to the file:
server {
    listen 80;
    server_name your_server_domain_or_IP;

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/pricing_app.sock;
    }

    location /static/ {
        alias /path/to/pricing_app/static/;
    }
}

# Enable the Nginx server block
sudo ln -s /etc/nginx/sites-available/pricing_app /etc/nginx/sites-enabled
sudo systemctl restart nginx
#!/usr/bin/env python
"""
Startup script for Render free tier deployment
This handles migrations and static files collection at startup
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

def run_startup_tasks():
    """Run Django startup tasks"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dboard.settings')
    django.setup()
    
    try:
        # Collect static files
        print("Collecting static files...")
        execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
        
        # Run migrations
        print("Running migrations...")
        execute_from_command_line(['manage.py', 'migrate'])
        
        print("Startup tasks completed successfully!")
        return True
    except Exception as e:
        print(f"Error during startup tasks: {e}")
        return False

if __name__ == '__main__':
    if run_startup_tasks():
        # Start gunicorn
        os.system('gunicorn dboard.wsgi:application --bind 0.0.0.0:$PORT')
    else:
        sys.exit(1)
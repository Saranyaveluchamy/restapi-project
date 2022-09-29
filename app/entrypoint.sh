#!/bin/sh
exec gunicorn --config /app/gunicorn_config.py main:flask_app
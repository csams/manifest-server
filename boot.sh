#!/usr/bin/env bash

# VENV=/opt/manifest_server
VENV=$PWD

source $VENV/bin/activate
exec gunicorn -b :8080 --access-logfile - --error-logfile - manifest_server:app

#!/usr/bin/env bash

source /opt/manifest-server/bin/activate
exec gunicorn -b :8080 --access-logfile - --error-logfile - manifest_server:app

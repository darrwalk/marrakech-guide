#!/bin/bash
set -e

# Use PORT environment variable if set, otherwise default to 10000
PORT=${PORT:-10000}

echo "Starting gunicorn on port $PORT"
exec gunicorn --bind 0.0.0.0:$PORT app:app
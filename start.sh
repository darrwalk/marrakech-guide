#!/bin/bash
set -e

# Use PORT from environment or default to 10000
PORT=${PORT:-10000}

echo "Starting Marrakech Travel Guide on port $PORT"
exec gunicorn --bind 0.0.0.0:$PORT app:app
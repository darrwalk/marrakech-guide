FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use PORT environment variable provided by Render
CMD gunicorn --bind 0.0.0.0:${PORT:-10000} app:app
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# SUPER SIMPLE test - no templates, no complex data
CMD ["python", "test_deploy.py"]
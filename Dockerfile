# Test fixture: an older base image and no non-root user, for SecureShip container/IaC scanning.
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]

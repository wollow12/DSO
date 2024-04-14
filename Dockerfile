# Stage 1: Build the Python Flask application using Gunicorn
FROM python:alpine3.19
WORKDIR /app
RUN adduser --disabled-password python
USER python

# Copy Python dependencies file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask application
COPY . .

CMD ["gunicorn", "--bind 0.0.0.0:9090 wsgi:app"]

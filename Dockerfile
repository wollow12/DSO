# Stage 1: Build the Python Flask application using Gunicorn
FROM python:slim
WORKDIR /app
RUN useradd -ms /bin/bash python
USER python

# Copy Python dependencies file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask application
COPY . .

CMD ["gunicorn", "--bind 0.0.0.0:9090 wsgi:app"]

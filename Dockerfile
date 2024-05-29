FROM python:alpine3.19
WORKDIR /app

# Copy Python dependencies file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask application
COPY . .

CMD ["python", "weather_app.py"]

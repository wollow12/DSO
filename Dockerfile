FROM python:3.9-alpine
WORKDIR /app

# Install curl
RUN apk update && apk add --no-cache curl

# Copy Python dependencies file and install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy Flask application
COPY . .

CMD ["python", "weather_app.py"]

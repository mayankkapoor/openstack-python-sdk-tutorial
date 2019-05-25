FROM python:3.7.3-slim

# Create app directory
WORKDIR /app

# Copy source code to app directory
COPY . /app
# Install needed packages
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "flaskr/app.py"]

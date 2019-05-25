FROM python:3.7.3-slim

# Create app directory
WORKDIR /app

# Copy source code to app directory
COPY . /app
# Install needed packages
RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT ["python", "flaskr/app.py"]

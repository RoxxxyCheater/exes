
# Use base Python
FROM python:3.9

# Set an environment variable to disable buffer output
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Installing project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


# Copying project code to a container
COPY . .
RUN pip install scrapy
# Running Django parser and server when container starts
CMD scrapy runspider reality_spider.py && python manage.py runserver 0.0.0.0:8000

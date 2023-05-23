FROM python:3.9

RUN apt-get update && apt-get install -y postgresql

WORKDIR /reality

# COPY requirements.txt /app/requirements.txt
# RUN pip install -r /app/requirements.txt

COPY . /reality

ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=qwerty
ENV POSTGRES_HOST=db

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]








https://github.com/orgs/A-Intelligence/people/RoxxxyCheater

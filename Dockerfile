# Используем базовый образ Python
FROM python:3.9

# Установка PostgreSQL и других зависимостей
RUN apt-get update && apt-get install -y postgresql

# Установка зависимостей Python
# COPY requirements.txt /requirements.txt
# RUN pip install -r /requirements.txt
RUN pip install psycopg2-binary
RUN pip install Django
RUN pip install scrapy
# Копирование файлов проекта
COPY . /reality

WORKDIR /reality

# Установка переменных окружения
ENV POSTGRES_DB=postgres
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=qwerty
ENV POSTGRES_HOST=127.0.0.1
# Определение команды запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
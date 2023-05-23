# Используем базовый образ Python
FROM python:3.9

# Установка PostgreSQL и других зависимостей
RUN apt-get update && apt-get install -y postgresql

# Установка зависимостей Python
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN pip install psycopg2-binary
RUN pip install Django
RUN pip install scrapy
# Копирование файлов проекта
COPY . /app

WORKDIR /app

# Установка переменных окружения
ENV POSTGRES_DB=product
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=qwerty
ENV POSTGRES_HOST=db-1
# Определение команды запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
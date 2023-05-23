
# Используйте базовый образ Python
FROM python:3.9

# Установите переменную среды для отключения вывода буфера
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Установка зависимостей проекта
COPY requirements.txt .
RUN pip install -r requirements.txt


# Копирование кода проекта в контейнер
COPY . .

# Запуск парсера и сервера Django при запуске контейнера
CMD scrapy runspider scrapers/sreality_spider.py && python manage.py runserver 0.0.0.0:8000
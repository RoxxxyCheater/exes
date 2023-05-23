
# Используйте базовый образ Python
FROM python:3.9

# Установите переменную среды для отключения вывода буфера
ENV PYTHONUNBUFFERED 1

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Установите зависимости проекта
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
# RUN pip install psycopg2
# Скопируйте код проекта в контейнер
COPY . .

# Запустите сервер Django при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
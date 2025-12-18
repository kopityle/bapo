# Используем готовый образ с Python
FROM python:3.10-alpine

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копируем все остальные файлы проекта (в нашем случае это app.py)
COPY . .

# Команда, которая будет выполняться при старте контейнера
CMD ["flask", "run", "--host=0.0.0.0"]
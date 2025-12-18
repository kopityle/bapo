import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# 1. Читаем переменную окружения 'TYPE'. 
# Если её нет, по умолчанию будет использоваться 'ip-api'.
API_TYPE = os.getenv('TYPE', 'ip-api')

@app.route('/')
def get_my_ip():
    try:
        # 2. В зависимости от значения переменной выбираем нужный URL
        if API_TYPE == 'jsonip':
            # Используем API от jsonip.com
            response = requests.get('https://jsonip.com/')
            response.raise_for_status() # Проверяем, что запрос прошел успешно
            # У этого API IP-адрес лежит в поле 'ip'
            ip_address = response.json().get('ip')
        else:
            # По умолчанию используем ip-api.com
            response = requests.get('http://ip-api.com/json/')
            response.raise_for_status()
            # У этого API IP-адрес лежит в поле 'query'
            ip_address = response.json().get('query')

        # 3. Возвращаем результат в нужном формате
        return jsonify({"myIP": ip_address})

    except requests.exceptions.RequestException as e:
        # Это обработка ошибок, если API недоступен
        return jsonify({"error": f"Не удалось подключиться к API: {e}"}), 503

# Стандартная строка для запуска Flask-приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
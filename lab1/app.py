import os
from flask import Flask, jsonify
from ip_services import IPServiceFactory

app = Flask(__name__)

API_TYPE = os.getenv('TYPE', 'ip-api')
ip_service = IPServiceFactory.create(API_TYPE)

@app.route('/')
def get_my_ip():
    try:
        ip_address = ip_service.get_ip()
        return jsonify({"myIP": ip_address})

    except Exception as e:
        return jsonify({"error": f"Ошибка сервиса: {str(e)}"}), 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)